# sqlalchemy-databricks

![pypi](https://img.shields.io/pypi/v/sqlalchemy-databricks.svg)
![pyversions](https://img.shields.io/pypi/pyversions/sqlalchemy-databricks.svg)

A SQLAlchemy Dialect for Databricks workspace and sql analytics clusters using the officially supported [databricks-sql-connector](https://pypi.org/project/databricks-sql-connector/) dbapi.

## Installation

Install using pip.

```bash
pip install sqlalchemy-databricks
```

## Usage

Installing registers the ``databricks+connector`` dialect/driver with SQLAlchemy. Fill in the required information when passing the engine URL. The http path can be for either a workspace or sql analytics cluster.

```python
from sqlalchemy import *
from sqlalchemy.engine import create_engine


engine = create_engine(
    "databricks+connector://token:<databricks_token>@<databricks_host>:443/<database_or_schema_name>",
    connect_args={
        "http_path": "<cluster_http_path>",
    },
)

logs = Table("my_table", MetaData(bind=engine), autoload=True)
print(select([func.count("*")], from_obj=logs).scalar())
```
