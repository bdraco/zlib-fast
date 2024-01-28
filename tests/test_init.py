import gzip as gzip_original
import zlib as zlib_original

from zlib_fast import disable, enable
from zlib_fast import gzip_adapter as best_gzip
from zlib_fast import zlib_adapter as best_zlib


def test_enable_disable():
    """Test enable/disable."""
    import gzip
    import zlib

    assert zlib is zlib_original
    assert gzip is gzip_original
    enable()
    import gzip
    import zlib

    assert zlib is best_zlib
    assert gzip is best_gzip
    disable()
    import gzip
    import zlib

    assert zlib is zlib_original
    assert gzip is gzip_original
