from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from providers.models import Provider
from django.db.models import Q, Count
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from cities_light.models import City
from .tables import CitiesTable

class DashboardView(SingleTableMixin,FilterView):
    template_name = 'dashboard/index.html'
    paginate_by = 10
    model = City
    table_class = CitiesTable
    fields = ('name',"region")

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        qs = qs.annotate(Count("providers")).order_by('-providers__count')
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["service_providers"] = Provider.objects.filter(~Q(services=None)).count()
        context["work_providers"] = Provider.objects.filter(~Q(works=None)).count()
        context["goods_providers"] = Provider.objects.filter(~Q(goods=None)).count()

        return context
