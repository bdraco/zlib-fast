__version__ = "0.1.0"

import sys
import zlib as zlib_original

from . import zlib_adapter as best_zlib


def enable() -> None:
    """Enable the adapter."""
    sys.modules["zlib"] = best_zlib


def disable() -> None:
    """Disable the adapter restore the original zlib."""
    sys.modules["zlib"] = zlib_original
