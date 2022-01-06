import os

import dotenv
import pytest

dotenv.load_dotenv(dotenv_path=dotenv.find_dotenv())

TOKEN = os.environ["DATABRICKS_TOKEN"]
HOST = os.environ["DATABRICKS_HOST"]
HTTP_PATH_WORKSPACE = os.environ["DATABRICKS_HTTP_PATH_WORKSPACE"]
HTTP_PATH_SQL_ANALYTICS = os.environ["DATABRICKS_HTTP_PATH_SQL_ANALYTICS"]


@pytest.fixture
def token():
    return TOKEN


@pytest.fixture
def host():
    return HOST


@pytest.fixture(params=[HTTP_PATH_WORKSPACE, HTTP_PATH_SQL_ANALYTICS])
def http_path(request):
    return request.param
