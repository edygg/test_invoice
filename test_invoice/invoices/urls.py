from django.urls import path
from .api import views as invoices_api_views


app_name = "invoices"

urlpatterns = [
    path("test/", view=invoices_api_views.TestApiView.as_view(), name="test"),
]