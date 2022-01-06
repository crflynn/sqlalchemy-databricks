from sqlalchemy import *
from sqlalchemy.engine import create_engine


def test_dialect(host, http_path, token):
    engine = create_engine(
        f"databricks+connector://token:{token}@{host}:443/default",
        connect_args={"http_path": f"{http_path}"},
    )
    tables = inspect(engine).get_table_names()
    print(tables)
