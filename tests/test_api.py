import pytest
from httpx import AsyncClient
from main import app
import json


class TestAPI:
    @pytest.mark.asyncio
    async def test_null_response(self):
        """
        Работает только на пустой БД!
        """
        request_schema = {
            "questions_num": 2,
        }
        async with AsyncClient(app=app, base_url="http://localhost:8000/v1") as ac:
            response_registration = await ac.post(
                f"/quiz/get_quiz",
                content=json.dumps(request_schema),
            )
        assert response_registration.status_code == 200
        assert response_registration.json() is None

    @pytest.mark.asyncio
    async def test_last_response(self):
        request_schema = {
            "questions_num": 2,
        }
        async with AsyncClient(app=app, base_url="http://localhost:8000/v1") as ac:
            response_registration = await ac.post(
                f"/quiz/get_quiz",
                content=json.dumps(request_schema),
            )
        assert response_registration.status_code == 200
        assert response_registration.json() is not None