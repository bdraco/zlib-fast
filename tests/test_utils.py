import pytest

from zlib_fast import utils


@pytest.mark.parametrize(
    ("in_level", "out_level"),
    [
        (-1, 2),
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 3),
        (8, 3),
        (9, 3),
    ],
)
def test_compression_mappings(in_level: int, out_level: int) -> None:
    """Test compression mappings."""
    assert utils.gzip_compress_level_to_isal(in_level) == out_level
