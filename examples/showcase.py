"""
This is a showcase of the terminal-style library.
It shows all the available colors and effects.

To run this file, use the following command:
python -m examples.showcase
"""

from terminal_style.terminal_style import (
    BACKGROUND_COLORS,
    FOREGROUND_COLORS,
    sprint,
    style,
)

print("\n--- Foreground Colors ---")
for color in list(FOREGROUND_COLORS.keys())[:6]:
    print(style(f"This is {color}", color=color))

print("\n--- Background Colors ---")
for color in list(BACKGROUND_COLORS.keys())[:6]:
    print(style(f"Background {color}", bg_color=color, color="white"))

print("\n--- Text Effects ---")
for effect in ["bold", "italic", "underline", "dim"]:
    kwargs = {effect: True}
    print(style(f"This is {effect}", color="cyan", **kwargs))

print("\n--- Combined Styles ---")
print(
    style(
        "Bold, Underlined, Red on Yellow",
        color="red",
        bg_color="yellow",
        bold=True,
        underline=True,
    )
)

print("\n--- Sprint Function ---")
sprint("Sprint in green!", color="green", bold=True)
