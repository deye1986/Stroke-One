#   >>>> urls in sim app folder, you are in the SIM folder <<<<

from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchView, name='searchView'),
    path('search/', views.searchView, name='searchView'),
    path('search/results/', views.searchResultsView, name='searchResultsView')
    ]