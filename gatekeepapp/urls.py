from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('guard/', views.guard_dashboard, name='guard_dashboard'),
    path('resident/', views.resident_dashboard, name='resident_dashboard'),
]