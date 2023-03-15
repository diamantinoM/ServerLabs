from datetime import date

from fastapi import APIRouter, Request, responses, status
from fastapi_chameleon import template


from common import (
    base_viewmodel_with,
    is_valid_name,
    is_valid_email,
    is_valid_password,
    is_valid_iso_date,
    form_field_as_str,
    find_in,
)
from services import student_service

MIN_DATE = date.fromisoformat('1920-01-01')

router = APIRouter()

@router.get('/account/register')                            
@template()
async def register():
    return register_viewmodel()


def register_viewmodel():
    return base_viewmodel_with({
       'name': '',
       'email': '',
       'password': '',
       'birth_date': '',
       'min_date': MIN_DATE,
       'max_date': date.today(),
       'checked': False,
    })


@router.post('/account/register')                            
@template(template_file='account/register.pt')
async def post_register(request: Request):
    vm = await post_register_viewmodel(request)

    if vm['error']:
       return vm
    
    response = responses.RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)
    return response


async def post_register_viewmodel(request: Request):
    def is_valid_birth_date(birth_date: str) -> bool:
        return(is_valid_iso_date(birth_date) and date.fromisoformat(birth_date) >= MIN_DATE)
    

    form_data = await request.form()
    name = form_field_as_str(form_data,'name')
    email = form_field_as_str(form_data, 'email')
    password = form_field_as_str(form_data, 'password')
    birth_date = form_field_as_str(form_data, 'birth_date')

    if not is_valid_name(name):
        error, error_msg = True, 'Nome inválido!'

    elif not is_valid_email(email):
        error, error_msg = True, 'Endereço de email inválido!'

    elif not is_valid_password(password):
        error, error_msg = True, 'Senha inválida!'

    elif not is_valid_birth_date(birth_date):
        error, error_msg = True, 'Data de nascimento inválida!'
    elif student_service.get_student_by_email(email):
        error, error_msg = True, f'Endereço de email {email} já existe!'
    else:
        error, error_msg = False, ''


    new_student_id = None
    if not error: 
        student = student_service.create_account(
            name,
            email,
            password,
            date.fromisoformat(birth_date),
        )
        new_student_id = student.id

    return base_viewmodel_with({
        'error': error,
        'error_msg': error_msg,
        'name': name,
        'email': email,
        'birth_date': birth_date,
        'min_date': MIN_DATE,
        'max_date': date.today(),
        'password': password,
        'checked': False,
        'user_id': new_student_id,
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