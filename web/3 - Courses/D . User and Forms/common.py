__all__ = (
    'base_viewmodel',
    'base_viewmodel_with',
    'is_valid_name',
    'form_field_as_str',
    'form_field_as_file',
    'is_valid_email',
    'is_valid_password',
    'is_valid_iso_date',
    'find_in'
)

from datetime import date
import re
from typing import Any, Iterable
from fastapi.datastructures import FormData
from fastapi import UploadFile


def base_viewmodel():
    return {
        'error': None,
        'error_msg': None,
        'user_id': None,
        'is_logged_in': False,
    }


def base_viewmodel_with(update_data) -> dict:
    vm = base_viewmodel()
    vm.update(update_data)
    return vm


def is_valid_name(name: str) -> bool:
    return all(part.isalpha() and len(part) > 2 for part in name.split())


def make_test_regex_fn(regex: str):
    compiled_regex = re.compile(regex)
    def test_regex_fn(value: str) -> bool:
        return bool(re.fullmatch(compiled_regex, value))
    return test_regex_fn

is_valid_email = make_test_regex_fn(
    r".*"
)

is_valid_password = make_test_regex_fn(
    r"[0-9a-zA-Z\$\#\?\.\!]{3,10}"
)


def is_valid_iso_date(iso_date: str) -> bool:
    try:
        date.fromisoformat(iso_date)
    except ValueError:
        return False
    else:   # noexception:
        return True


def find_in(iterable: Iterable, predicate) -> Any | None:
    return next((obj for obj in iterable if predicate(obj)), None)


def form_field_as_str(form_data: FormData, field_name: str) -> str:
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str')


def form_field_as_file(form_data: FormData, field_name: str) -> UploadFile:
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is not UploadFile')