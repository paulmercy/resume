from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.index, name="index"),
	path('portfolio_detail/<str:slug>/', views.portfolio_detail, name='portfolio_detail'),
	]
