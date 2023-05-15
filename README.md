# ⚠️ This project is archived. A new SQLAlchemy dialect is available directly from Databricks

Databricks now maintain a SQLAlchemy dialect in the https://github.com/databricks/databricks-sql-python repository.  You can install it with `pip install databricks-sql-python`. This new dialect was introduced in `databricks-sql-python==2.4.0`. 

The SQLAlchemy URI format for this connector is:

```
databricks://token:dapi***@***.cloud.databricks.com?http_path=/sql/***
```

There is a self-contained usage example available in the `examples` directory of that repository.

Please direct any issues / pull requests to that repository and Databricks support. 


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

In the above example:

* `databricks_host` is the Databricks instance host name.
* `cluster_http_path` is the HTTP Path from your [Connection Details](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#get-connection-details-for-a-sql-warehouse) screen:
    - For a Databricks SQL Warehouse the format is `/sql/1.0/endpoints/***************`
    - For a Databricks Runtime interactive cluster the format is `/sql/protocolv1/o/**************/****-*******-*******`
* `databricks_token` is the Databricks [Personal Access Token](https://docs.databricks.com/dev-tools/api/latest/authentication.html#token-management) for the account that will execute commands and queries
