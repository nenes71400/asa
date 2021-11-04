from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


from base.models import Tournoi

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticate_user = True
    
    def get_success_url(self):
        return reverse_lazy('tournois')


class TournoiList(LoginRequiredMixin, ListView):
    model = Tournoi
    context_object_name = 'tournois'
    template_name = 'base/tournois.html'

"""
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tournois'] = context['tournois'].filter(user=self.request.user)
        context['count'] = context['tournois'].filter(complete=False).count
        return context
"""

class TournoiDetail(LoginRequiredMixin, DetailView):
    model = Tournoi
    context_object_name = 'tournoi'
    template_name = 'base/tournoi.html'

class TournoiCreate(LoginRequiredMixin, CreateView):
    model = Tournoi
    fields = '__all__'
    success_url = reverse_lazy('tournois')

class TournoiUpdate(LoginRequiredMixin, UpdateView):
    model = Tournoi
    fields = '__all__'
    success_url = reverse_lazy('tournois')

class TournoiDelete(LoginRequiredMixin, DeleteView):
    model = Tournoi
    context_object_name = 'tournoi'
    success_url = reverse_lazy('tournois')



"""

from django.http import HttpResponse
def tournoiList(request):
    return HttpResponse('Liste des Tournois')

"""