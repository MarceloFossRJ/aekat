from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="app/templates")

# Start FastApi
app = FastAPI()

# Mount the static files directory (CSS, JavaScript, images)
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse, summary="Home page")
def home(request: Request):
    try:
        my_list = "Hello"
        response = templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"mylist": my_list}
        )
        return response
    except Exception as e:
        return f"Error loading template: {str(e)}", 500

@app.post("/submit_search", response_class=HTMLResponse)
def search_result(request: Request, search: str = Form(...)):
        context = {"request": request, "search": search }

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context=context
        )

