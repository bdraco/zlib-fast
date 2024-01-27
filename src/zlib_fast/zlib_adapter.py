from typing import Any, Optional

from isal import isal_zlib
from isal.isal_zlib import (
    DEF_BUF_SIZE,
    DEF_MEM_LEVEL,
    DEFLATED,
    MAX_WBITS,
    Z_BEST_COMPRESSION,
    Z_BEST_SPEED,
    Z_DEFAULT_COMPRESSION,
    Z_DEFAULT_STRATEGY,
    Z_FILTERED,
    Z_FINISH,
    Z_FIXED,
    Z_FULL_FLUSH,
    Z_HUFFMAN_ONLY,
    Z_NO_FLUSH,
    Z_RLE,
    Z_SYNC_FLUSH,
    Compress,
    Decompress,
    adler32,
    compress,
    crc32,
    crc32_combine,
    decompress,
    decompressobj,
    error,
)


def compressobj(
    level: int = isal_zlib.Z_DEFAULT_COMPRESSION,
    method: int = isal_zlib.DEFLATED,
    wbits: int = isal_zlib.MAX_WBITS,
    memLevel: int = isal_zlib.DEF_MEM_LEVEL,
    strategy: int = isal_zlib.Z_DEFAULT_STRATEGY,
    zdict: Optional[Any] = None,
) -> isal_zlib.Compress:
    """Compressobj adapter to convert zlib level to isal compression level."""
    if level < 0 or level > 9:
        raise ValueError(f"Invalid compression level: {level}")

    if level <= 3:
        level = isal_zlib.Z_BEST_SPEED
    elif level <= 6:
        level = isal_zlib.Z_DEFAULT_COMPRESSION
    else:
        level = isal_zlib.Z_BEST_COMPRESSION

    if zdict is not None:
        return isal_zlib.compressobj(
            level,
            method,
            wbits,
            memLevel,
            strategy,
            zdict,
        )

    return isal_zlib.compressobj(
        level,
        method,
        wbits,
        memLevel,
        strategy,
    )


__all__ = (
    "DEF_BUF_SIZE",
    "DEF_MEM_LEVEL",
    "DEFLATED",
    "MAX_WBITS",
    "Z_BEST_COMPRESSION",
    "Z_BEST_SPEED",
    "Z_DEFAULT_COMPRESSION",
    "Z_DEFAULT_STRATEGY",
    "Z_FILTERED",
    "Z_FINISH",
    "Z_FIXED",
    "Z_FULL_FLUSH",
    "Z_HUFFMAN_ONLY",
    "Z_NO_FLUSH",
    "Z_RLE",
    "Z_SYNC_FLUSH",
    "Compress",
    "Decompress",
    "adler32",
    "compress",
    "crc32",
    "crc32_combine",
    "decompress",
    "decompressobj",
    "error",
    "compressobj",
)
