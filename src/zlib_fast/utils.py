from isal import isal_zlib


def gzip_compress_level_to_isal(level: int) -> int:
    """Convert a gzip compression level to an isal compression level."""
    if level == -1:
        return isal_zlib.Z_DEFAULT_COMPRESSION
    if level < 0 or level > 9:
        raise ValueError(f"Invalid compression level: {level}")
    if level <= 1:
        return 0
    if level <= 3:
        return 1
    elif level <= 6:
        return 2
    return 3
