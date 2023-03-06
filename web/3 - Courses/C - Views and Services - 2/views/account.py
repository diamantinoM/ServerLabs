from fastapi_chameleon import template
from fastapi import APIRouter

router = APIRouter()

@router.get('/account')
async def index():
    return {}


@router.get('/account/login')
@template()
async def login():
    return {
        'error': False,
        'error_msg': 'There was an error with your data. Please try again.'
    }


@router.get('/account/register')
@template()
async def register():
    return {
        'error': False,
        'error_msg': 'There was an error with your data. Please try again.'
    }