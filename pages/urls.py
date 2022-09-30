from django.urls import path
from .views import ContactPageView, HomePageView, InformationPageView

urlpatterns = [
    path("", HomePageView.as_view(), name = "index"),
    path("contact", ContactPageView.as_view(), name = "contact"),
    path("information", InformationPageView.as_view(), name = "information")
]