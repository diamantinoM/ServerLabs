from fastapi import APIRouter
from fastapi_chameleon import template
from common import base_viewmodel_with

router = APIRouter()

@router.get('/account/register')                            
@template()
async def register():
    return register_viewmodel()


def register_viewmodel():
    return base_viewmodel_with({
        'error': False,
        'error_msg': 'There was an error with your data. Please try again.',
    })


@router.get('/account/login')                            
@template()
async def login():
    return login_viewmodel()


def login_viewmodel():
    return base_viewmodel_with({
        'error': None,
        # 'error_msg': 'There was an error with your data. Please try again.',
    })


@router.get('/account')                            
async def index():
    return {

    }