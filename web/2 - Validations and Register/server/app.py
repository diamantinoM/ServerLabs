"""
In this version we use both Pydantic and SQLAlchemy:

    1. Pydantic: For defining, parsing and validating data exposed by the
    Web API

    2. SQLAlchemy: To define and use the SQL data model.

In the next version we'll use SQLModel to bridge the gap between Pydantic
and SQLAlchemy.

We'll also use the common layering and file structure recommend for FastAPI
and Flask apps:

    - schemas.py: Pydantic models/schemas
    - models.py: SQLAlchemy models (the data model)
    - database_crud.py: SQLAlchemy database access operations
    - database.py: SQLAlchemy connection and session definitions

Links:
    https://fastapi.tiangolo.com/tutorial/sql-databases/
    https://docs.sqlalchemy.org/en/14/orm/quickstart.html
    https://docs.sqlalchemy.org/en/14/orm/
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import database as db
import database_crud as crud
import schemas as sch
import models
from schemas import ErrorCode


app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8080",
]

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_session():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.post('/register', response_model = sch.PlayerRegisterResult)
async def register(
        player: sch.PlayerRegister,
        db_session: Session = Depends(get_db_session),
):
    
    tourn_id = player.tournament_id
    if tourn_id is None:
        error = ErrorCode.ERR_UNSPECIFIED_TOURNAMENT
        raise HTTPException(status_code = 400, detail=error.details())

    db_player = crud.get_player_by_email(db_session, player.email)
    if not db_player:
        db_player = crud.create_player(db_session, player)

    if db_player.tournament_id == tourn_id:
        error = ErrorCode.ERR_PLAYER_ALREADY_ENROLLED
        raise HTTPException(status_code=400, detail=error.details(tourn_id = tourn_id))

    if crud.get_tournament_by_id(db_session, tourn_id) is None:
        error = ErrorCode.ERR_UNKNOWN_TOURNAMENT_ID
        raise HTTPException(status_code = 404, detail=error.details(tourn_id = tourn_id))

    crud.update_player_tournament(db_session, db_player, tourn_id)

    return db_player
    

def main():
    import uvicorn 
    from docopt import docopt
    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll
for tournaments.

Usage:
  app.py [-c | -c -d] [-p PORT] [-h HOST_IP] [-r]

Options: 
  -p PORT, --port=PORT              Listen on this port [default: 8000]
  -c, --create-ddl                  Create datamodel in the database
  -d, --populate-db                 Populate the DB with dummy for testing purposes
  -h HOST_IP, --host=HOST_IP        Listen on this IP address [default: 127.0.0.1]
  -r, --reload                      Reload app
"""
    args = docopt(help_doc)
    create_ddl = args['--create-ddl']
    populate_db = args['--populate-db']
    if create_ddl:
        db.create_metadata()
        if populate_db:
            models.populate_db()

    uvicorn.run('app:app', 
                port = int(args['--port']),
                host = args['--host'], 
                reload = args['--reload'],
            )


if __name__ == '__main__':
    main()