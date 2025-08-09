"""
Main application module for the FastAPI application.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.views import home as home_views
from app.api import v1 as api_v1

# Create FastAPI application instance
app = FastAPI(
    title="AI Firstly",
    description="AI Firstly application",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request
                                                     , "title": "Welcome to AI Firstly!"})



# Routers
app.include_router(home_views.router, prefix="", tags=["pages"])
app.include_router(api_v1.router, prefix="/api/v1", tags=["api"])

#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=8000)
