from django.shortcuts import render

# Create your views here.


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid
