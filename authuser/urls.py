from django.urls import path
from .views import signup, BookCreateView
urlpatterns = [
    path("register/",  signup ),
    path('addBook', BookCreateView.as_view() )
]
