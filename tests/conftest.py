from pathlib import Path
import sys

from argparse import Namespace
from configparser import ConfigParser
import pytest
from pytest_postgresql import factories

sys.path.append(str(Path(__file__).parent.parent))
from backend.__main__ import create_app

BASE_DIR = Path(__file__).parent.resolve()

postgresql_my_proc = factories.postgresql_proc()

postgresql_my = factories.postgresql(
    "postgresql_proc",
    load=[str(BASE_DIR.joinpath("database/test_database.sql"))],
)


@pytest.fixture(scope="function", autouse=True)
def setup_database(postgresql_my):
    return postgresql_my


@pytest.fixture
def base_args():
    config = ConfigParser()
    config.read(BASE_DIR.joinpath("pytest.ini"))

    db_host = config.get("pytest", "postgresql_host")
    db_name = config.get("pytest", "postgresql_dbname")
    db_port = config.get("pytest", "postgresql_port")
    db_user = config.get("pytest", "postgresql_user")
    db_password = config.get("pytest", "postgresql_password")

    base_args_ = Namespace(
        host="localhost",
        port=8080,
        db_host=db_host,
        db_name=db_name,
        db_port=db_port,
        db_user=db_user,
        db_password=db_password,
        db_url=f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
        log_sql=False,
    )
    return base_args_


@pytest.fixture
def cli(event_loop, aiohttp_client, base_args):
    return event_loop.run_until_complete(aiohttp_client(create_app(base_args)))


@pytest.fixture
def templates():
    return [
        {
            "id": 1,
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Stadtbild_M%C3%BCnchen.jpg/2560px-Stadtbild_M%C3%BCnchen.jpg",
            "description": "just a picture",
            "title": "just a picture",
            "address": "some address",
        },
        {
            "id": 2,
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bratskfountain.jpg/300px-Bratskfountain.jpg",
            "description": "just a picture of Bratsk",
            "title": "just a picture of Bratsk",
            "address": "some address",
        },
    ]
