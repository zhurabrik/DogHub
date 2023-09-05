from http import HTTPStatus
import pytest


@pytest.mark.asyncio
async def test_post_template(cli):
    data = {"some_test_date": "SomeTestData"}
    handler = "/template"
    response = await cli.post(handler, json=data)

    assert response.status == HTTPStatus.OK

    body = await response.json()

    assert body["id"] == 3

    data["id"] = 3

    response = await cli.get(handler, params={"template_id": 3})

    assert response.status == HTTPStatus.OK

    assert await response.json() == data
