__all__ = (
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
