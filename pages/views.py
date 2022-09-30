from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name: str = "index.html"

class ContactPageView(TemplateView):
    template_name: str = "contact.html"

class InformationPageView(TemplateView):
    template_name: str = "information.html"