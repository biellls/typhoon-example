
def build_s3_key(system_name: str, entity: str, part_num: int, ds: str, etl_timestamp: str, extension: str) -> str:
    return f'{system_name}/{entity}/{ds}/{etl_timestamp}_{entity}_part{part_num}.{extension.replace(".", "")}'
