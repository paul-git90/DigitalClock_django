from django.urls import path
from clock_digital.views import digital_clock

urlpatterns = [
    path('', digital_clock, name='clock_digital'),
]
