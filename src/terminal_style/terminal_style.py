"""Terminal style package for formatting and styling terminal output.

This package provides utilities for adding colors, background colors, and text effects
to terminal output. It includes functions for both printing styled text and returning
styled strings.
"""

from pathlib import Path
from typing import Any

import yaml


class TerminalStyleConfig:
    """Manages terminal style configuration and provides access to style settings."""

    def __init__(self):
        """Initialize the configuration manager."""
        self.config_file = Path(__file__).parent / "terminal_style_config.yml"
        self._config: dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """Load configuration from YAML file."""
        try:
            with open(self.config_file, encoding="utf-8") as file:
                self._config = yaml.safe_load(file)
                # Decode escape sequences
                for section in ["foreground_colors", "background_colors", "text_effects"]:
                    if section in self._config:
                        self._config[section] = {
                            k: v.encode("utf-8").decode("unicode_escape")
                            for k, v in self._config[section].items()
                        }
                if "reset" in self._config:
                    self._config["reset"] = (
                        self._config["reset"].encode("utf-8").decode("unicode_escape")
                    )
        except (FileNotFoundError, yaml.YAMLError):
            self._config = {}

    @property
    def reset(self) -> str:
        """Get the reset ANSI code."""
        return self._config.get("reset", "\033[0m")

    @property
    def foreground_colors(self) -> dict[str, str]:
        """Get the foreground colors mapping."""
        return self._config.get("foreground_colors", {})

    @property
    def background_colors(self) -> dict[str, str]:
        """Get the background colors mapping."""
        return self._config.get("background_colors", {})

    @property
    def text_effects(self) -> dict[str, str]:
        """Get the text effects mapping."""
        return self._config.get("text_effects", {})


# Initialize configuration
_config = TerminalStyleConfig()

# Create convenient access variables
RESET = _config.reset
FOREGROUND_COLORS = _config.foreground_colors
BACKGROUND_COLORS = _config.background_colors
TEXT_EFFECTS = _config.text_effects


# -------------------------- utils ----------------------------------------


def sprint(*args, color=None, bg_color=None, **effects_and_kwargs):
    """
    Print text with comprehensive styling options.

    Args:
        *args: Text to print (same as regular print)
        color (str, optional): Foreground color name
        bg_color (str, optional): Background color name
        **effects_and_kwargs: Text effects (bold, italic, underline, etc.) and print kwargs
    """
    # Separate print kwargs from effect kwargs
    print_kwargs = {}
    effect_kwargs = {}

    for key, value in effects_and_kwargs.items():
        if key in ["sep", "end", "file", "flush"]:
            print_kwargs[key] = value
        else:
            effect_kwargs[key] = value

    # Build style codes
    style_codes = []

    # Add foreground color
    if color and color.lower() in FOREGROUND_COLORS:
        style_codes.append(FOREGROUND_COLORS[color.lower()])

    # Add background color
    if bg_color and bg_color.lower() in BACKGROUND_COLORS:
        style_codes.append(BACKGROUND_COLORS[bg_color.lower()])

    # Add text effects
    for effect_name, effect_value in effect_kwargs.items():
        if effect_value and effect_name.lower() in TEXT_EFFECTS:
            style_codes.append(TEXT_EFFECTS[effect_name.lower()])

    # Combine all style codes
    style_prefix = "".join(style_codes)

    # Apply styling to text
    if style_prefix:
        styled_args = []
        for arg in args:
            styled_args.append(f"{style_prefix}{arg}{RESET}")
        print(*styled_args, **print_kwargs)
    else:
        # No styling, just regular print
        print(*args, **print_kwargs)


def style(text, color=None, bg_color=None, **effects):
    """
    Return styled text string without printing.

    Args:
        text (str): Text to style
        color (str, optional): Foreground color name
        bg_color (str, optional): Background color name
        **effects: Text effects (bold, italic, underline, etc.)

    Returns:
        str: Styled text with ANSI codes

    Examples:
        styled_text = style("Hello", color="pink", bold=True)
        error_text = style("Error", color="red", bg_color="yellow", bold=True)
    """
    style_codes = []

    # Add foreground color
    if color and color.lower() in FOREGROUND_COLORS:
        style_codes.append(FOREGROUND_COLORS[color.lower()])

    # Add background color
    if bg_color and bg_color.lower() in BACKGROUND_COLORS:
        style_codes.append(BACKGROUND_COLORS[bg_color.lower()])

    # Add text effects
    for effect_name, effect_value in effects.items():
        if effect_value and effect_name.lower() in TEXT_EFFECTS:
            style_codes.append(TEXT_EFFECTS[effect_name.lower()])

    style_prefix = "".join(style_codes)

    if style_prefix:
        return f"{style_prefix}{text}{RESET}"
    else:
        return text


def list_available_styles():
    """
    Print all available colors and effects for reference.
    """
    print("=== Available Foreground Colors ===")
    for color_name in sorted(FOREGROUND_COLORS.keys()):
        sprint(f"{color_name}", color=color_name)

    print("\n=== Available Background Colors ===")
    for bg_color_name in sorted(BACKGROUND_COLORS.keys()):
        sprint(f"  {bg_color_name}  ", bg_color=bg_color_name, color="white")

    print("\n=== Available Text Effects ===")
    for effect_name in sorted(TEXT_EFFECTS.keys()):
        effect_kwargs = {effect_name: True}
        sprint(f"{effect_name}", **effect_kwargs)


if __name__ == "__main__":
    list_available_styles()
