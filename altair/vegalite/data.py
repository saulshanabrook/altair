
from toolz.curried import curry, pipe
from ..utils.core import sanitize_dataframe
from ..utils.data import (
    MaxRowsError, limit_rows, sample, to_csv, to_json, to_values,
    check_data_type, DataTransformerRegistry, to_url
)


@curry
def default_data_transformer(data, max_rows=5000):
    return pipe(data, to_url, limit_rows(max_rows=max_rows), to_values)


__all__ = (
    'DataTransformerRegistry',
    'MaxRowsError',
    'curry',
    'sanitize_dataframe',
    'default_data_transformer',
    'limit_rows',
    'pipe',
    'sample',
    'to_csv',
    'to_json',
    'to_values',
    'check_data_type'
)
