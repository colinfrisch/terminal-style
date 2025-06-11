<p align="center">
  <img src="https://raw.githubusercontent.com/colinfrisch/terminal-style/main/resources/banner.png" width="400" alt="logo">
</p>

# Terminal Style - simple text styling for your terminal

| | |
| --- | --- |
| Package | [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![PyPI](https://img.shields.io/pypi/v/terminal-style.svg)](https://pypi.org/project/terminal-style) [![PyPI Downloads](https://static.pepy.tech/badge/terminal-style)](https://pepy.tech/projects/terminal-style) [![PyPI - License](https://img.shields.io/pypi/l/terminal-style)](https://pypi.org/project/terminal-style/) |
| Meta | [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |

Styling text in a terminal is a pain and weirdly, there are no libraries that are both simple to use and multi-task for this. So I made a very simple lightweight Python library for styling terminal text with colors, backgrounds, and text effects. No complex features, no hassle.

**install using pip:** `pip install -U terminal-style`

## Using terminal-style : 3 tools that will make your life easier


- **`sprint`** acts like `print` but allows you to style the text :
```python
sprint("Hello, world!", color="red", bold=True)
```
<img src="https://raw.githubusercontent.com/colinfrisch/terminal-style/main/resources/sprint_demo.png" width="200" alt="logo">

<br/><br/>

- **`style`** is a function that returns a styled string formatted terminal use. Can be used in regular print statements :
```python
print(
  style("Hello", color="red", bold=True),
  style("old", color="blue", italic=True),
  style("friend", color="green", underline=True),
  style("!", color="yellow", bold=True),
)
```
<img src="https://raw.githubusercontent.com/colinfrisch/terminal-style/main/resources/style_demo.png" width="150" alt="logo">

<br/><br/>


- **`spinner`** is a function that will show a spinner in the terminal : the spinner will stop automatically when a next line is printed in the terminal. It runs in parallel, so don't worry about blocking the main thread.
```python
spinner("Processing...", color="cyan", bold=True, type="dots")
```
<img src="https://raw.githubusercontent.com/colinfrisch/terminal-style/main/resources/spinner_demo.png" width="150" alt="logo">

<br/><br/>


## Available Styles

| color/bg_color | Spinner | Text Effect |
|-------|---------|-------------|
| black ![](https://placehold.co/15x15/000000/000000.png) | dots `⠋` | bold |
| red ![](https://placehold.co/15x15/FF0000/FF0000.png) | line `\|` | dim |
| green ![](https://placehold.co/15x15/00FF00/00FF00.png) | arrow `←` | italic |
| yellow ![](https://placehold.co/15x15/FFFF00/FFFF00.png) | bouncingBar `[    ]` | underline |
| blue ![](https://placehold.co/15x15/0000FF/0000FF.png) | bouncingBall `( ●    )` | blink |
| magenta/purple ![](https://placehold.co/15x15/FF00FF/FF00FF.png) | earth `🌍` | reverse |
| cyan ![](https://placehold.co/15x15/00FFFF/00FFFF.png) | moon `🌑` | hidden |
| white ![](https://placehold.co/15x15/FFFFFF/FFFFFF.png) | weather `☀️` | strikethrough |
| bright_black/gray/grey ![](https://placehold.co/15x15/808080/808080.png) | hearts `💛` | strike |
| bright_red ![](https://placehold.co/15x15/FF6666/FF6666.png) | growHorizontal `▏`  | double_underline |
| bright_green ![](https://placehold.co/15x15/66FF66/66FF66.png) | modern `▰▱▱▱▱▱▱` | overline |
| bright_yellow ![](https://placehold.co/15x15/FFFF66/FFFF66.png) | growVertical `▁` | |
| bright_blue ![](https://placehold.co/15x15/6666FF/6666FF.png) | | |
| bright_magenta ![](https://placehold.co/15x15/FF66FF/FF66FF.png) | | |
| bright_purple ![](https://placehold.co/15x15/FF66FF/FF66FF.png) | | |
| bright_cyan ![](https://placehold.co/15x15/66FFFF/66FFFF.png) | | |
| bright_white ![](https://placehold.co/15x15/FFFFFF/FFFFFF.png) | | |
| orange ![](https://placehold.co/15x15/FFA500/FFA500.png) | | |
| pink ![](https://placehold.co/15x15/FFC0CB/FFC0CB.png) | | |
| light_pink ![](https://placehold.co/15x15/FFB6C1/FFB6C1.png) | | |
| deep_pink ![](https://placehold.co/15x15/FF1493/FF1493.png) | | |
| lime ![](https://placehold.co/15x15/32CD32/32CD32.png) | | |
| gold ![](https://placehold.co/15x15/FFD700/FFD700.png) | | |
| navy ![](https://placehold.co/15x15/000080/000080.png) | | |
| maroon ![](https://placehold.co/15x15/800000/800000.png) | | |
| olive ![](https://placehold.co/15x15/808000/808000.png) | | |
| teal ![](https://placehold.co/15x15/008080/008080.png) | | |
| silver ![](https://placehold.co/15x15/C0C0C0/C0C0C0.png) | | |
| brown ![](https://placehold.co/15x15/A52A2A/A52A2A.png) | | |
| indigo ![](https://placehold.co/15x15/4B0082/4B0082.png) | | |
| violet ![](https://placehold.co/15x15/EE82EE/EE82EE.png) | | |
| turquoise ![](https://placehold.co/15x15/40E0D0/40E0D0.png) | | |
| coral ![](https://placehold.co/15x15/FF7F50/FF7F50.png) | | |
| salmon ![](https://placehold.co/15x15/FA8072/FA8072.png) | | |
| khaki ![](https://placehold.co/15x15/F0E68C/F0E68C.png) | | |
| crimson ![](https://placehold.co/15x15/DC143C/DC143C.png) | | |
| forest_green ![](https://placehold.co/15x15/228B22/228B22.png) | | |
| sky_blue ![](https://placehold.co/15x15/87CEEB/87CEEB.png) | | |
| lavender ![](https://placehold.co/15x15/E6E6FA/E6E6FA.png) | | |
| peach ![](https://placehold.co/15x15/FFDAB9/FFDAB9.png) | | |
| mint ![](https://placehold.co/15x15/98FF98/98FF98.png) | | |



## Incoming Features

- automatic indentation of text
- pre-built styles for common use cases
- support for custom styles


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

**Author** : Colin Frisch - [linkedin.com/colinfrisch](https://www.linkedin.com/in/colinfrisch/)

---

*Make your terminal output beautiful and readable with terminal-style!*
