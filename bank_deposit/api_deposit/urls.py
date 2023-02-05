from django.urls import path

from .views import deposit_calculation

urlpatterns = [
    path('deposits/', deposit_calculation, name='deposits')
]
