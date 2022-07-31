from django.urls import path
from .views import recipes_view


urlpatterns = [
    path('', recipes_view),
]
