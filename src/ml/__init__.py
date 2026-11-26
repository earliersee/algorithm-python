"""Classic algorithms implemented in Python."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("algorithm-python")
except PackageNotFoundError:  # running directly from the source tree
    __version__ = "0.1.0"

__all__ = ["__version__"]
