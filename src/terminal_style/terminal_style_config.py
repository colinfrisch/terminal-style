from pathlib import Path
from typing import Any

import yaml


class TerminalStyleConfig:
    """Manages terminal style configuration and provides access to style settings."""

    def __init__(self):
        """Initialize the configuration manager."""
        self.config_file = Path(__file__).parent / "config_styles.yml"
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

    @property
    def spinners(self) -> dict[str, list[str]]:
        """Get the spinner configurations mapping."""
        return self._config.get("spinners", {})
