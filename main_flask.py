# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Set up templates (for HTML files)
templates = Jinja2Templates(directory="templates")

# Optional: Serve static files (CSS, JS, images) from a 'static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve index.html at the root path
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the server when script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1979)