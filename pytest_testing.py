import pytest


def test_employee_name():
    name = "Maruthi"
    assert name != ""


def test_employee_id():
    employee_id = "EMP001"
    assert employee_id != ""


def test_employee_salary():
    salary = 25000
    assert salary > 0


def test_invalid_salary():
    salary = 0
    assert salary <= 0
