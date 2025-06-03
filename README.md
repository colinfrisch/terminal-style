<p align="center">
  <img src="https://github.com/colinfrisch/terminal-style/blob/main/resources/banner.png" width="400" alt="logo">
</p>

# Terminal Style - simple text styling for your terminal

| Feature | Status |
|---------|--------|
| Package | [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) |
| License | [![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) |
| Meta | [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Ruff](https://img.shields.io/badge/Ruff-v0.0.292-purple.svg)](https://github.com/charliermarsh/ruff) |

Styling text in a terminal is a pain and weirdly, there are no great libraries for this. So I made a very simple lightweight Python library for styling terminal text with colors, backgrounds, and text effects. No complex features, no hassle.

## Using terminal-style

**install using pip:**
```bash
pip install terminal-style
```
**Requirements**

- Python 3.10+
- PyYAML


**The two main functions are `sprint` and `style`.**

- `sprint` is a wrapper around `print` that allows you to style the text.

- `style` is a function that returns a styled string.


## Available Colors

| Category | Available Styles |
|----------|-----------------|
| Colors/Backgrounds | ![](https://placehold.co/15x15/000000/000000.png) ![](https://placehold.co/15x15/0000FF/0000FF.png) ![](https://placehold.co/15x15/808080/808080.png) ![](https://placehold.co/15x15/0088FF/0088FF.png) ![](https://placehold.co/15x15/00FFFF/00FFFF.png) ![](https://placehold.co/15x15/00FF00/00FF00.png) ![](https://placehold.co/15x15/FF00FF/FF00FF.png) ![](https://placehold.co/15x15/FF0000/FF0000.png) ![](https://placehold.co/15x15/FFFFFF/FFFFFF.png) ![](https://placehold.co/15x15/FFFF00/FFFF00.png) ![](https://placehold.co/15x15/008800/008800.png) ![](https://placehold.co/15x15/A52A2A/A52A2A.png) ![](https://placehold.co/15x15/FF7F50/FF7F50.png) ![](https://placehold.co/15x15/DC143C/DC143C.png) ![](https://placehold.co/15x15/FF1493/FF1493.png) ![](https://placehold.co/15x15/228B22/228B22.png) ![](https://placehold.co/15x15/FFD700/FFD700.png) ![](https://placehold.co/15x15/4B0082/4B0082.png) ![](https://placehold.co/15x15/F0E68C/F0E68C.png) ![](https://placehold.co/15x15/E6E6FA/E6E6FA.png) ![](https://placehold.co/15x15/FFB6C1/FFB6C1.png) ![](https://placehold.co/15x15/800000/800000.png) ![](https://placehold.co/15x15/98FF98/98FF98.png) ![](https://placehold.co/15x15/000080/000080.png) ![](https://placehold.co/15x15/808000/808000.png) ![](https://placehold.co/15x15/FFA500/FFA500.png) ![](https://placehold.co/15x15/FFDAB9/FFDAB9.png) ![](https://placehold.co/15x15/FFC0CB/FFC0CB.png) ![](https://placehold.co/15x15/FA8072/FA8072.png) ![](https://placehold.co/15x15/C0C0C0/C0C0C0.png) ![](https://placehold.co/15x15/87CEEB/87CEEB.png) ![](https://placehold.co/15x15/008080/008080.png) ![](https://placehold.co/15x15/40E0D0/40E0D0.png) ![](https://placehold.co/15x15/EE82EE/EE82EE.png) |
| Text Effects | <blink>blink</blink>, **bold**, <span style="opacity:0.5">dim</span>, *italic*, <span style="text-decoration:overline">overline</span>, <span style="filter:invert(100%)">reverse</span>, ~~strikethrough~~, <u>underline</u>, hidden (not here duh) |

## Usage

### print styled text with `sprint`

```python
# Combine multiple effects
sprint("Important Notice", color="yellow", bg_color="red", bold=True, underline=True)

# Use with print parameters
sprint("Loading...", color="cyan", end="")  # No newline
sprint("Done!", color="green")

# Extended color palette
sprint("Beautiful", color="pink", italic=True)
sprint("Ocean", color="turquoise", bold=True)
```

### get styled text with `style`
```python
from terminal_style import style

# Create styled strings for use in larger text
error_text = style("ERROR", color="red", bold=True)
warning_text = style("WARNING", color="yellow", bold=True)

print(f"[{error_text}] Something went wrong!")
print(f"[{warning_text}] This is a warning message")
```

## Development

Contributions are welcome! Please feel free to submit a Pull Request.

```bash
git clone https://github.com/colinfrisch/terminal-style
cd terminal-style
pip install -e .
```

Install development dependencies:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
# or
python run_tests.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Author** : Colin Frisch - [colin.frisch@gmail.com](mailto:colin.frisch@gmail.com)

---

*Make your terminal output beautiful and readable with terminal-style!*
