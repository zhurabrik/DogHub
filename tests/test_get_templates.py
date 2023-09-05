from http import HTTPStatus
import pytest


@pytest.mark.asyncio
async def test_get_templates(cli, templates):
    handler = "/templates"
    response = await cli.get(handler)

    assert response.status == HTTPStatus.OK

    body = await response.json()

    assert body["templates"] == templates


@pytest.mark.asyncio
@pytest.mark.parametrize("limit, offset", [(1, 0), (2, 1)])
async def test_get_templates_limit_offset(cli, templates, limit, offset):
    handler = "/templates"
    params = {"limit": limit, "offset": offset}
    response = await cli.get(handler, params=params)

    assert response.status == HTTPStatus.OK

    body = await response.json()

    assert body["templates"] == templates[offset : offset + limit]
