from django.urls import path
from . import views
from .views import login_view
urlpatterns = [
    path('dashboard/', views.dashboard_with_pivot, name='dashboard'),
    path('', views.login_view, name='login'),
    path('data', views.pivot_data, name='pivot_data'),
]