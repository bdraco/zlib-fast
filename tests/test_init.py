import zlib as zlib_original

from zlib_fast import disable, enable
from zlib_fast import zlib_adapter as best_zlib


def test_enable_disable():
    """Test enable/disable."""
    import zlib

    assert zlib is zlib_original
    enable()
    import zlib

    assert zlib is best_zlib
    disable()
    import zlib

    assert zlib is zlib_original
