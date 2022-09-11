from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	# path('', views.IndexView.as_view(), name="home"),
	path('', views.index, name="index"),
	path('category-portfolio-list/<int:cat_id>',views.category_portfolio_list,name='category-portfolio-list'),
	# path('contact/', views.ContactView, name="contact")
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	]