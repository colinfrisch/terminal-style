"""Terminal style package for formatting and styling terminal output.

This package provides utilities for adding colors, background colors, and text effects
to terminal output. It includes functions for both printing styled text and returning
styled strings.
"""

from src.terminal_style.terminal_style_config import TerminalStyleConfig

# Initialize configuration
_config = TerminalStyleConfig()

# Create convenient access variables
RESET = _config.reset
FOREGROUND_COLORS = _config.foreground_colors
BACKGROUND_COLORS = _config.background_colors
TEXT_EFFECTS = _config.text_effects


# -------------------------- utils ----------------------------------------


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

    # Apply styling to each argument using the existing style() function
    styled_args = []
    for arg in args:
        styled_arg = style(str(arg), color=color, bg_color=bg_color, **effect_kwargs)
        styled_args.append(styled_arg)

    # Print the styled arguments
    print(*styled_args, **print_kwargs)


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
    # CL to execute : python -m src.terminal_style.terminal_style
    list_available_styles()
    sprint("Hello", color="red", bg_color="orange", bold=True)
