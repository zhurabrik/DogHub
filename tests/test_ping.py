from http import HTTPStatus
import pytest


@pytest.mark.asyncio
async def test_ping(cli):
    handler = "/ping"
    assert (await cli.get(handler)).status == HTTPStatus.OK


@pytest.mark.asyncio
async def test_ping_db(cli):
    handler = "/ping_db"
    assert (await cli.get(handler)).status == HTTPStatus.OK
