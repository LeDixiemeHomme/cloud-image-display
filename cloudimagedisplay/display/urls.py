from django.urls import path

from .views import (
    index,
    display_view
)

urlpatterns = [
    path('<str:url>', display_view, name='display_view'),
    path('', index, name='index'),
]