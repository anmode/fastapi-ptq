# tests/test_main.py
import re
import httpx
import respx
import unittest
from app.main import app
from httpx import AsyncClient


SAMPLE_SUCCESS = {
    "data": [
        {"Title": "Maze Runner: The Scorch Trials", "Year": 2015, "imdbID": "tt4046784"},
        {"Title": "Into the Grizzly Maze", "Year": 2015, "imdbID": "tt1694021"},
    ]
}
SAMPLE_EMPTY = {"data": []}


class MoviesEndpointTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Any common async fixtures can go here
        pass

    @respx.mock
    async def test_get_movies_success(self):
        year = 2015
        respx.get(re.compile(r"/api/moviesdata.*")).respond(200, json=SAMPLE_SUCCESS)

        async with AsyncClient(app=app, base_url="http://test") as ac:
            resp = await ac.get(f"/movies/{year}")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "titles": [
                    "Maze Runner: The Scorch Trials",
                    "Into the Grizzly Maze",
                ]
            },
        )

    @respx.mock
    async def test_get_movies_no_results(self):
        year = 2100
        respx.get(re.compile(r"/api/moviesdata.*")).respond(200, json=SAMPLE_EMPTY)

        async with AsyncClient(app=app, base_url="http://test") as ac:
            resp = await ac.get(f"/movies/{year}")

        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.json()["detail"], "No Results Found")
