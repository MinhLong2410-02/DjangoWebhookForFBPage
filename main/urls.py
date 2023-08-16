from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('verify/', VerifyView.as_view(), name='verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
