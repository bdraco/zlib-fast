from zlib_fast import zlib_adapter


def test_compressobj():
    assert zlib_adapter.compressobj() is not None


def test_decompressobj():
    assert zlib_adapter.decompressobj() is not None
