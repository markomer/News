from django.urls import path
from .views import (FrontPageView, SportsPageView, SocietyPageView, BusinessPageView)

urlpatterns = [
  path('front/', FrontPageView.as_view(), name='front'),
  path('sports/', SportsPageView.as_view(), name='sports'),
  path('society/', SocietyPageView.as_view(), name='society'),
  path('business/', BusinessPageView.as_view(), name='business'),
]  