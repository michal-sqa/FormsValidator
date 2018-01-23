import manage_forms
import pytest

def compose_error_message(environment):
    error_message = "\nMissing forms attributes for specified workflows and content types: "
    for value in manage_forms.get_missing_form_attributes(environment):
        error_message += f"\n{value}"
    return error_message

def test_absent_form_attributes(environment):
    assert len(manage_forms.get_missing_form_attributes(environment)) == 0, compose_error_message(environment)