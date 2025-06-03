"""Tests for the terminal_style package."""

from terminal_style.terminal_style import (
    BACKGROUND_COLORS,
    FOREGROUND_COLORS,
    RESET,
    TEXT_EFFECTS,
    TerminalStyleConfig,
    list_available_styles,
    sprint,
    style,
)


def test_terminal_style_config_initialization():
    """Test that TerminalStyleConfig initializes correctly."""
    config = TerminalStyleConfig()
    assert isinstance(config.reset, str)
    assert isinstance(config.foreground_colors, dict)
    assert isinstance(config.background_colors, dict)
    assert isinstance(config.text_effects, dict)


def test_style_basic_colors():
    """Test basic color styling."""
    # Test foreground color
    styled_text = style("test", color="red")
    assert styled_text.startswith(FOREGROUND_COLORS["red"])
    assert styled_text.endswith(RESET)

    # Test background color
    styled_text = style("test", bg_color="blue")
    assert styled_text.startswith(BACKGROUND_COLORS["blue"])
    assert styled_text.endswith(RESET)

    # Test both colors
    styled_text = style("test", color="green", bg_color="yellow")
    assert FOREGROUND_COLORS["green"] in styled_text
    assert BACKGROUND_COLORS["yellow"] in styled_text
    assert styled_text.endswith(RESET)


def test_style_text_effects():
    """Test text effects styling."""
    # Test single effect
    styled_text = style("test", bold=True)
    assert TEXT_EFFECTS["bold"] in styled_text
    assert styled_text.endswith(RESET)

    # Test multiple effects
    styled_text = style("test", bold=True, italic=True, underline=True)
    assert TEXT_EFFECTS["bold"] in styled_text
    assert TEXT_EFFECTS["italic"] in styled_text
    assert TEXT_EFFECTS["underline"] in styled_text
    assert styled_text.endswith(RESET)


def test_style_invalid_colors():
    """Test handling of invalid color names."""
    # Test invalid foreground color
    styled_text = style("test", color="invalid_color")
    assert styled_text == "test"

    # Test invalid background color
    styled_text = style("test", bg_color="invalid_color")
    assert styled_text == "test"


def test_style_invalid_effects():
    """Test handling of invalid effect names."""
    styled_text = style("test", invalid_effect=True)
    assert styled_text == "test"


def test_style_empty_text():
    """Test styling of empty text."""
    styled_text = style("", color="red", bold=True)
    assert styled_text.startswith(FOREGROUND_COLORS["red"])
    assert TEXT_EFFECTS["bold"] in styled_text
    assert styled_text.endswith(RESET)


def test_style_no_styling():
    """Test text with no styling applied."""
    text = "test"
    styled_text = style(text)
    assert styled_text == text


def test_sprint_basic(capsys):
    """Test basic sprint functionality."""
    sprint("test", color="red")
    captured = capsys.readouterr()
    assert captured.out.startswith(FOREGROUND_COLORS["red"])
    assert captured.out.endswith(RESET + "\n")


def test_sprint_multiple_args(capsys):
    """Test sprint with multiple arguments."""
    sprint("test1", "test2", color="blue")
    captured = capsys.readouterr()
    assert FOREGROUND_COLORS["blue"] in captured.out
    assert "test1" in captured.out
    assert "test2" in captured.out
    assert captured.out.endswith(RESET + "\n")


def test_sprint_print_kwargs(capsys):
    """Test sprint with print keyword arguments."""
    sprint("test", color="green", end="")
    captured = capsys.readouterr()
    assert captured.out.startswith(FOREGROUND_COLORS["green"])
    assert captured.out.endswith(RESET)


def test_list_available_styles(capsys):
    """Test the list_available_styles function."""
    list_available_styles()
    captured = capsys.readouterr()
    assert "Available Foreground Colors" in captured.out
    assert "Available Background Colors" in captured.out
    assert "Available Text Effects" in captured.out
