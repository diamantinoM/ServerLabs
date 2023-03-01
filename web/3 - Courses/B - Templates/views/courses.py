from fastapi_chameleon import template
from fastapi import APIRouter

router = APIRouter()

@router.get('/courses')
async def courses():
    return {}