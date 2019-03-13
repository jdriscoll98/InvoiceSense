from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView, DeleteView
from .models import *
# Create your views here.
class CompanyHomepage(LoginRequiredMixin, TemplateView):
    template_name = 'company/homepage.html'

    def get_context_data(self, **kwargs):
        employee = Employee.objects.get(user=self.request.user)
        context = {
            'company': employee.company
        }
        return context
