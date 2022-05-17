from django.urls import path
from .views import HomePageView, AboutPageView, AccountsPageView, ArticlesPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about/', AboutPageView.as_view(), name='about'),
  path('accounts/', AccountsPageView.as_view(), name='accounts'),
  path('articles/', ArticlesPageView.as_view(), name='articles'),
 
]