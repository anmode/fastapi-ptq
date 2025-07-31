
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
BASE_URL = "https://jsonmock.hackerrank.com/api/moviesdata"


async def fetch_movies(year: int) -> list[str]:
    """Fetch movie data asynchronously and return list of titles."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(BASE_URL, params={"Year": year})
    resp.raise_for_status()
    payload = resp.json()
    return [m["Title"] for m in payload.get("data", [])]


@app.get("/movies/{year}")
async def get_movies(year: int):
    titles = await fetch_movies(year)
    if not titles:
        raise HTTPException(status_code=404, detail="No Results Found")
    return {"titles": titles}
