from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from main.mixins import RedirectUnauthenticatedMixin
from users.forms import CreateUserForm


class CreateUserView(FormView):
    template_name = 'registration/create_user.html'
    form_class = CreateUserForm
    success_url = '/users/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileView(RedirectUnauthenticatedMixin, DetailView):
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        print(self.request.user)
        return self.request.user
