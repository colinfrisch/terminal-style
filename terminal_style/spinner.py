import atexit
import builtins
import threading
import time

from terminal_style.terminal_style import style
from terminal_style.terminal_style_config import TerminalStyleConfig

# Global spinner state
_current_spinner = None
_original_print = builtins.print


def _cleanup_spinner():
    """Clean up spinner on program exit."""
    if _current_spinner and _current_spinner.running:
        _current_spinner.running = False
        if _current_spinner.thread and _current_spinner.thread.is_alive():
            _current_spinner.thread.join(timeout=0.1)


# Register cleanup function to run on program exit
atexit.register(_cleanup_spinner)


def _stop_current_spinner():
    """Stop the currently running spinner if any."""
    global _current_spinner  # noqa: PLW0603
    if _current_spinner and _current_spinner.running:
        _current_spinner.stop()
    _current_spinner = None


def _patched_print(*args, **kwargs):
    """Patched print function that stops spinner before printing."""
    _stop_current_spinner()
    return _original_print(*args, **kwargs)


# Patch the built-in print function
builtins.print = _patched_print


class SpinnerThread:
    """Background spinner thread."""

    def __init__(self, text="", color=None, bg_color=None, type="line", **effects):
        self.text = text
        self.color = color
        self.bg_color = bg_color
        self.effects = effects

        # Load spinner configurations from YAML config
        config = TerminalStyleConfig()
        spinners_config = config.spinners

        # Get the specific spinner type, default to "line" if not found
        if type in spinners_config:
            self.spinner_chars = spinners_config[type]
        else:
            # Fallback to line spinner if type not found
            self.spinner_chars = spinners_config.get("line", ["|", "/", "-", "\\"])

        self.running = False
        self.thread = None

    def _spin(self):
        """Internal spinning loop."""
        i = 0
        while self.running:
            current_char = self.spinner_chars[i % len(self.spinner_chars)]
            display_text = f"{current_char} {self.text}" if self.text else current_char

            # Apply styling if provided
            if self.color or self.bg_color or self.effects:
                display_text = style(
                    display_text, color=self.color, bg_color=self.bg_color, **self.effects
                )

            _original_print(f"\r{display_text}", end="", flush=True)
            time.sleep(0.2)
            i += 1

    def start(self):
        """Start the spinner."""
        self.running = True
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def stop(self):
        """Stop the spinner."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=0.2)
        _original_print()  # Move to next line


def spinner(text="", color=None, bg_color=None, type="line", **effects):
    """
    Start a spinner that automatically stops when the next print occurs.

    Args:
        text (str): Text to display after the spinner
        color (str, optional): Foreground color name
        bg_color (str, optional): Background color name
        type (str): Type of spinner animation (loaded from config_styles.yml)
        **effects: Text effects (bold, italic, underline, etc.)

    Available spinner types (from config_styles.yml):
        dots, line, arrow, bouncingBar, bouncingBall, earth, moon,
        weather, hearts, runner, pong, modern, growVertical, growHorizontal

    Examples:
        spinner("Loading...")
        # Do some work...
        print("Done!")  # Spinner automatically stops and this prints

        spinner("Processing...", color="cyan", bold=True, type="dots")
        process_data()
        print("Complete!")  # Spinner stops automatically
    """
    global _current_spinner  # noqa: PLW0603

    # Stop any existing spinner
    _stop_current_spinner()

    # Start new spinner
    _current_spinner = SpinnerThread(text, color, bg_color, type, **effects)
    _current_spinner.start()


def stop_spinner():
    """Manually stop the current spinner."""
    _stop_current_spinner()


if __name__ == "__main__":
    # CL to execute : python -m src.terminal_style.spinner
    spinner("Loading...", color="cyan", bold=True, type="bouncingBall")
    time.sleep(1)
    print("Done!")
