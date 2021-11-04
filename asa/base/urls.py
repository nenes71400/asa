from django.urls import path
from .views import TournoiList, TournoiDetail, TournoiCreate, TournoiUpdate, TournoiDelete, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('', TournoiList.as_view(), name='tournois'),
    path('tournoi/<int:pk>/', TournoiDetail.as_view(), name='tournoi'),
    path('tournoi-create/', TournoiCreate.as_view(), name='tournoi-create'),
    path('tournoi-update/<int:pk>/', TournoiUpdate.as_view(), name='tournoi-update'),
    path('tournoi-delete/<int:pk>/', TournoiDelete.as_view(), name='tournoi-delete'),

]


"""

from . import views

urlpatterns = [
    path('', views.tournoiList, name='tournoi')
]
"""
