"""Pandas "proxy" package."""
from typing import TYPE_CHECKING

from awswrangler._distributed import MemoryFormatEnum, memory_format

if TYPE_CHECKING or memory_format.get() == MemoryFormatEnum.PANDAS:
    from pandas import *  # noqa: F403

    # Explicit import because mypy doesn't support forward references to a star import
    from pandas import (  # noqa: F401
        DataFrame,
        Series,
        concat,
        isna,
        isnull,
        json_normalize,
        notna,
        read_csv,
        read_excel,
        to_datetime,
    )
elif memory_format.get() == MemoryFormatEnum.MODIN:
    from modin.pandas import *  # noqa: F403

    # Explicit import because mypy doesn't support forward references to a star import
    from modin.pandas import (  # noqa: F401
        DataFrame,
        Series,
        concat,
        isna,
        isnull,
        json_normalize,
        notna,
        read_csv,
        read_excel,
        to_datetime,
    )
else:
    raise ImportError(f"Unknown memory format {memory_format}")


__all__ = [
    "DataFrame",
    "Series",
    "concat",
    "isna",
    "isnull",
    "json_normalize",
    "notna",
    "read_csv",
    "read_excel",
    "to_datetime",
]
