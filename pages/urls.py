from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us', views.AboutUsPageView.as_view(), name='about-us'),
]
