from django.shortcuts import render
from django.views.generic.edit import FormView

from users.forms import CreateUserForm


class CreateUserView(FormView):
    template_name = 'registration/create_user.html'
    form_class = CreateUserForm
    success_url = '/'
