from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('contact/', views.contact, name = "contact-page"),
    path('about/', views.about, name="about-page"),
    path('search/', views.search, name="search-page"),
    path('game/', views.game, name="game-page"),
    path("blogs/", views.blogs, name="blog-page"),
    path("discussion/", views.discussion, name="discussion-page")

]
