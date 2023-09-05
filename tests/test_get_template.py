from http import HTTPStatus
import pytest


@pytest.mark.asyncio
async def test_get_template(cli, templates):
    handler = "/template"
    params = {"template_id": 1}
    response = await cli.get(handler, params=params)

    assert response.status == HTTPStatus.OK

    body = await response.json()

    assert body == templates[0]


@pytest.mark.asyncio
async def test_get_template_error(cli):
    handler = "/template"
    params = {"template_id": 5}
    response = await cli.get(handler, params=params)

    assert response.status == HTTPStatus.NOT_FOUND
