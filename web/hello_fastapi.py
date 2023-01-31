# Gravar como 'hello_fastapi.py'
# Executar:
#       $ uvicorn hello_fastapi:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World!"}
#:

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"2xitem_id": item_id * 2, "q": q}
#:

@app.get("/soma/{x}/{y}")
async def sum(x: int, y: int):
    return {"x + y": x + y}
#:

# Por omissão FastAPI gera JSON

# Protocolo HTTP possui um conjunto de métodos (isto é, de mensagens):
#   - GET: obter um recurso (ler)
#   - POST: enviar dados para o servidor / criar um registo no servidor
#   - PUT: semelhante a POST mas dados são enviados como um upload
#   - DELETE: apagar recursos no lado do servidor
#   - HEAD
#   - etc.

# Exercício: 
#       1. Correr no vosso repositório o hello_fastapi.py (c/ uvicorn)
#       2. Testar
#       3. Acrescentar função para receber dois parâmetros x e y e devolver
#          a soma de x com y. A função deve ser acessível por get e o caminho
#          deve começar com "/soma". A função deve-se chamar "sum".
#