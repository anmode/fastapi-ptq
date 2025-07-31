
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
BASE_URL = "https://jsonmock.hackerrank.com/api/moviesdata"

@app.get("/movies/{year}")
async def get_movies(year: int):
    """Return list of movie titles for given year.

    * Call the external API with ?Year=<year>
    * Extract 'Title' from each object in the `data` array
    * Return {"titles": [...]} preserving order
    * If no movies found, raise 404 with detail "No Results Found"
    """
    # 👉 TODO: Implement me!
    raise NotImplementedError("Implement the movies endpoint")
