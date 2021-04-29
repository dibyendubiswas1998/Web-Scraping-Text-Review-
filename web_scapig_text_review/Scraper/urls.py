from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("db/", views.DB, name="Db"),
    path("review/<int:id>/", views.Review, name="Review"),
    path('delete/<int:id>/', views.Delete, name="Delete"),
]
