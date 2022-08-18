from django.urls import path
from . import views
from .views import (
    postView,
    postDetailView,
    postCreateView,
    postUpdateView,
    postDeleteView
)


urlpatterns = [
    path('', postView.as_view(), name='blog-home'),
    path('', postView.as_view(), name='homePage'),
    path('post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('about/', views.aboutPage, name='blog-about'),
    path('post/add', postCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', postUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', postDeleteView.as_view(), name='post-delete'),
]
