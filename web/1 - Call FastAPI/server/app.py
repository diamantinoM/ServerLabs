from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()
# app.mount("/static", StaticFiles(directory="../client"), name="static")

# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

################################################################################

@app.get('/hello1')
async def hello1(name: str):
    return f"Hello: {name}"
#:

@app.post('/hello2')
async def hello2(request: Request):
    # https://fastapi.tiangolo.com/advanced/using-request-directly/
    # https://www.starlette.io/requests/
    form_data = await request.form()
    return f"Hello: {form_data['name']}"
#:

################################################################################

@app.get('/hello3/{name}')
async def hello3(name: str):
    return f"Hello: {name}"
#:

# https://fastapi.tiangolo.com/tutorial/body/
class NameArgs(BaseModel):
    name: str
#:

@app.post('/hello4')
async def hello4(name: NameArgs):
    return f"Hello: {name.name}"
#:

################################################################################


################################################################################

def main(): 
    import uvicorn
    uvicorn.run('app:app', port=8000, log_level='info', reload=True)
#:

if __name__ == '__main__':
    main()
#:
