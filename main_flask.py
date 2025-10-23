# main_flask.py
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import signal

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Graceful shutdown handler (optional)
def signal_handler(signum, frame):
    print("\nShutting down gracefully...")
    os._exit(0)

if __name__ == "__main__":
    # Register signal handler for clean exit (works with kill)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    uvicorn.run(app, host="0.0.0.0", port=1979, log_level="info")