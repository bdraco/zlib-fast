from isal import isal_zlib


def gzip_compress_level_to_isal(level: int) -> int:
    """Convert a gzip compression level to an isal compression level."""
    if level < 0 or level > 9:
        raise ValueError(f"Invalid compression level: {level}")
    if level <= 3:
        return isal_zlib.Z_BEST_SPEED
    elif level <= 6:
        return isal_zlib.Z_DEFAULT_COMPRESSION
    return isal_zlib.Z_BEST_COMPRESSION
