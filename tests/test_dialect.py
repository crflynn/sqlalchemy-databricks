from sqlalchemy import *
from sqlalchemy.engine import create_engine


def test_dialect(host, http_path, token):
    engine = create_engine(
        f"databricks+connector://token:{token}@{host}:443/default",
        connect_args={"http_path": f"{http_path}"},
    )
    tables = inspect(engine).get_table_names()
    print(tables)


def test_has_table(host, http_path, token):
    engine = create_engine(
        f"databricks+connector://token:{token}@{host}:443/default",
        connect_args={"http_path": f"{http_path}"},
    )

    engine.dialect.has_table(engine, 'table_name_that_should_not_exist')


def test_create_table_with_primary_key():
    def raise_if_primary_key(sql, *multiparams, **params):
        ddl_statement =  str(sql.compile(dialect=engine.dialect))
        if 'primary' in ddl_statement.lower():
            raise ValueError(f'{ddl_statement=}')

    engine = create_mock_engine(
        f"databricks+connector://token:test@test:443/default",
        raise_if_primary_key
    )

    metadata_obj = MetaData()

    test = Table(
        'test',
        metadata_obj,
        Column('test_id', Integer, primary_key=True)
    )

    metadata_obj.create_all(engine)
