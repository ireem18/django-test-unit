# cases/urls.py
from django.urls import path
from .views import CaseOperationView

urlpatterns = [
    path("case", CaseOperationView.as_view(), name="case"),
]