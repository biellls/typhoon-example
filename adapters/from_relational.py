from io import BytesIO

from typhoon.contrib.functions.relational import ExecuteQueryResult
from typhoon.contrib.transformations.db_result import to_csv

from transformations.data_lake import build_s3_key


def to_s3_write_csv(data: ExecuteQueryResult, system_name, ds: str, etl_timestamp: str):
    csv_data = to_csv(description=data.columns, data=data.batch)
    out = dict(
        data=BytesIO(csv_data.encode('utf_8')),
        path=build_s3_key(system_name, data.table_name, data.batch_num, ds, etl_timestamp, '.csv'),
    )
    return out
