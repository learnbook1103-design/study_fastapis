from fastapi import FastAPI

app = FastAPI()

from routes.todos import router as todos_router
app.include_router(todos_router, prefix="/todos")

# http://localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://localhost:8000/html
@app.get("/html")
async def root_html():
    html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Jeong</title>
        </head>
        <body>
            <div>My name is Jeong!</div>
        </body>
        </html>
        '''
#     return html_content

from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates/")

# http://localhost:8000/main.html
@app.get("/main.html")
async def main_html(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# http://192.168.0.65:8000/toyproject.html
@app.get("/toyproject.html")
async def main_html(request: Request):
    return templates.TemplateResponse("toyproject.html", {"request": request})

# http://192.168.0.65:8000/main_html_context
@app.get("/main_html_context")
async def main_html_content(request: Request):
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple","Banana","Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }
    return templates.TemplateResponse("main_html_context.html", context)

# http://localhost:8000/users/list
@app.get("/users/list")
async def user_list(request:Request) :
    users = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 28, "city": "Daegu"}
    ]

    context = {
        "request": request
        , "user_list" : users
    }
    return templates.TemplateResponse("users/list.html", context)

# http://localhost:8000/jina2
@app.get("/jina2")
async def products_list(request:Request) :
    products = [
    {"name": "Laptop", "price": 1200, "tags": ["electronics", "office"]},
    {"name": "Smartphone", "price": 800, "tags": ["mobile", "electronics"]},
    {"name": "Keyboard", "price": 100,"tags": ["accessories"]}
    ]
    context = {
        "request": request
        , "products_list" : products
    }
    return templates.TemplateResponse("jina2.html", context)

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post.
@app.get("/board/detail_json")
async def board_details_json(request: Request):
    params = dict(request.query_params)
    return {"title": params["title"], "content": params["content"]}

# http://localhost:8000/board/detail_post_json?title=Third%20Post&content=This%20is%20the%20third%20post.
@app.post("/board/detail_post_json")
async def board_details_json(request: Request):
    params = dict(await request.form())
    return {"title": params["title"], "content": params.get("content")}

# http://localhost:8000/board/detail_html
@app.get("/board/detail_html")
async def main_html(request: Request):
    return templates.TemplateResponse("boards/detail.html", {"request": request})

# http://localhost:8000/board/detail_html/{detail_id}
@app.get("/board/detail_html/{detail_id}")
async def main_html(request: Request, detail_id):
    return templates.TemplateResponse("boards/detail.html", {"request": request})

# 정적 파일 설정
from fastapi.staticfiles import StaticFiles
app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

pass