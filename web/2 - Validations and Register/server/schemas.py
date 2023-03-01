"""
In this module we define the Pydantic models. While these models are
used to interface FastAPI with http clients, SQLAlchemy models 
are used to talk to the database.

NOTE: There will some code duplication because some attributes will
have to be defined twice, once for the Pydantic models, and once for
SQLAlchemy. In another coming example, we will introduce a new library
that will bridge the two libraries, and prevent some of the code
duplication that happens when you use Pydantic and SQLAlchemy
separately.

We will create an PlayerBase Pydantic models (or let's say "schemas") 
to have common attributes while creating or reading data.

And create an PlayerRegister that inherit from it (so they will have 
the same attributes), plus any additional data (attributes) needed for
creation.

So, the user will also have a password when creating it. But for 
security, the password won't be in other Pydantic models, for example,
it won't be sent from the API when reading a user.
"""

from enum import Enum

from pydantic import BaseModel, Field


class PlayerBase(BaseModel):
    full_name: str
    email: str

    class Config:
        # https://docs.pydantic.dev/usage/model_config/
        # https://docs.pydantic.dev/usage/models/#orm-mode-aka-arbitrary-class-instances
        orm_mode = True
    


# NOTE: Notice that SQLAlchemy models define attributes using '=', and
# pass the type as a parameter to Column like in: 
#
#   name = Column(String)
#
# Whereas, Pydantic models declare the types using Python native types 
# and annotates them with ':', the notation used in Python to declare
# types:
#
#   name: str
#
# Have it in mind, so you don't get confused when using '=' and ':' with 
# them.

class PlayerRegister(PlayerBase):
    password: str
    phone_number: str | None = Field(
        title="Local portuguese phone number or international prefixed w/ +XYZ country code"
    )
    birth_date: str | None
    level: str
    tournament_id: int | None


class PlayerRegisterResult(PlayerBase):
    id: int


class ErrorCode(Enum):
    ERR_UNSPECIFIED_TOURNAMENT = 'Missing tournament id.'
    ERR_PLAYER_ALREADY_ENROLLED = 'Player already enrolled in tournament'
    ERR_UNKNOWN_TOURNAMENT_ID = 'Unknown tournament id'

    def details(self, **kargs) -> dict:
        details_dict = {'error_code': self.name, 'error_msg': self.value}
        details_dict.update(kargs)
        return details_dict
    

