from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("web.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/web.html")
async def web():
    raise HTTPException(
        status_code=404,
        detail="Not Found"
    )
