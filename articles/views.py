from django.views.generic import TemplateView


class FrontPageView(TemplateView):
  template_name = 'articles/front.html'

class SportsPageView(TemplateView):
  template_name = 'articles/sports.html'


class SocietyPageView(TemplateView):
  template_name = 'articles/society.html'

class BusinessPageView(TemplateView):
  template_name = 'articles/business.html'
