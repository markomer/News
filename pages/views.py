from django.views.generic import TemplateView



class HomePageView(TemplateView):
  template_name = 'pages/home.html'

class AboutPageView(TemplateView):
  template_name = 'pages/about.html'

class AccountsPageView(TemplateView):
  template_name = 'pages/accounts.html'
