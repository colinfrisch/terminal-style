#!/usr/bin/env python3
"""
Terminal Style Package Showcase
===============================

This example demonstrates the three main functions of the terminal-style package:
1. style() - Return styled text strings
2. sprint() - Print text with styling
3. spinner() - Display animated loading spinners

Install the package with: pip install terminal-style
"""

import time

from terminal_style import spinner, sprint, style


def main():
    """Showcase the main terminal-style functions."""

    print("=" * 60)
    print("🎨 TERMINAL STYLE PACKAGE SHOWCASE")
    print("=" * 60)

    # ===========================================
    # 1. STYLE FUNCTION DEMO
    # ===========================================
    print("\n1. STYLE FUNCTION - Returns styled strings")
    print("-" * 45)

    # Basic color styling
    hello_text = style("Hello, World!", color="cyan", bold=True)
    warning_text = style("WARNING", color="yellow", bg_color="red", bold=True)
    success_text = style("SUCCESS", color="bright_green", underline=True)

    print(f"Basic styling: {hello_text}")
    print(f"Warning style: {warning_text}")
    print(f"Success style: {success_text}")

    # Advanced styling combinations
    fancy_text = style(
        "Fancy Text", color="pink", bg_color="navy", bold=True, italic=True
    )
    error_text = style("ERROR 404", color="bright_red", strikethrough=True, blink=True)

    print(f"Fancy combo: {fancy_text}")
    print(f"Error style: {error_text}")

    # ===========================================
    # 2. SPRINT FUNCTION DEMO
    # ===========================================
    print("\n 2. SPRINT FUNCTION - Direct styled printing")
    print("-" * 48)

    sprint("This is a basic colored message", color="blue")
    sprint("Bold and underlined text", color="magenta", bold=True, underline=True)
    sprint("Background colored text", color="white", bg_color="green", bold=True)

    # Multiple arguments with styling
    sprint(
        "Processing file:",
        "data.txt",
        "- Status:",
        "Complete ✓",
        color="cyan",
        sep=" ",
        end="\n",
    )

    # Different text effects
    sprint("Italic text example", color="purple", italic=True)
    sprint("Dim text example", color="gray", dim=True)
    sprint("Reverse colors", color="yellow", bg_color="blue", reverse=True)

    # ===========================================
    # 3. SPINNER FUNCTION DEMO
    # ===========================================
    print("\n3. SPINNER FUNCTION - Animated loading indicators")
    print("-" * 52)

    # Basic spinner
    print("Basic line spinner:")
    spinner("Loading basic data...", color="cyan")
    time.sleep(1.5)

    # Dots spinner with styling
    print("\nDots spinner with styling:")
    spinner("Processing files...", color="yellow", bold=True, type="dots")
    time.sleep(1.5)

    # Bouncing ball spinner
    print("\nBouncing ball animation:")
    spinner("Analyzing data...", color="green", type="bouncingBall")
    time.sleep(1.5)

    # Earth spinner (emoji)
    print("\nEarth spinner:")
    spinner("Syncing with servers...", color="blue", bold=True, type="earth")
    time.sleep(1.5)

    # Modern progress bar style
    print("\nModern progress bar:")
    spinner("Downloading updates...", color="purple", type="modern")
    time.sleep(1.5)

    # Hearts spinner with background
    print("\nHearts spinner with background:")
    spinner("Spreading love...", color="red", bg_color="white", type="hearts")
    time.sleep(1.5)

    # COMBINING ALL FUNCTIONS ------------------------------------------------------------

    print("\nCombining all functions")
    print("-" * 35)

    # Create styled messages
    start_msg = style("Starting final demo...", color="bright_cyan", bold=True)
    print(start_msg)

    # Use spinner for "work"
    spinner(
        "Running complex calculations...", color="orange", bold=True, type="growVertical"
    )
    time.sleep(1.5)

    # Print results with sprint
    sprint(
        "Demo completed successfully!",
        color="bright_green",
        bold=True,
        bg_color="navy",
    )
    sprint("Thank you for trying terminal-style!", color="pink", italic=True)

    print("\n" + "=" * 60)
    sprint(
        "Learn more: https://github.com/colinfrisch/terminal-style",
        color="cyan",
        underline=True,
    )
    print("=" * 60)


if __name__ == "__main__":
    # CL to execute : python -m examples.showcase
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nShowcase interrupted.")
    except Exception as e:
        error_msg = style(f"Error: {e}", color="red", bold=True)
        print(f"\n{error_msg}")
