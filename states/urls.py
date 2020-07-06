
from django.urls import path

from .views import StateListView, StateDetailView, StateLGAView


urlpatterns = [
    path('', StateListView.as_view(), name='state-list'),
    path('<str:slug>/', StateDetailView.as_view(), name='state-detail'),
    path('<str:slug>/lga/', StateLGAView.as_view(), name='state-lga-list'),
]
