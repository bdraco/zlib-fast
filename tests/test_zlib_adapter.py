import pytest

from zlib_fast import zlib_adapter


def test_compressobj():
    assert zlib_adapter.compressobj() is not None
    assert zlib_adapter.compressobj(zdict=b"") is not None
    with pytest.raises(ValueError, match="Invalid compression level: -80"):
        zlib_adapter.compressobj(level=-80)
    for level in range(10):
        zlib_adapter.compressobj(level=level)


def test_decompressobj():
    assert zlib_adapter.decompressobj() is not None
