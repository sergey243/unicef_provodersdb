from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.utils.translation import gettext as _
from django.core.serializers import serialize
from .models import Provider, Service, Work, Good, GoodsProvided, ServicesProvided, WorkExecuted
from .tables import ProviderTable, ServicesTable, WorksTable, GoodsTable
from .filters import ProviderFilter, ServiceFilter, GoodFilter, WorkFilter
from .forms import ProviderForm,ServiceForm, GoodForm, WorkForm, EvaluationForm


#Providers views
class ProvidersList(SingleTableMixin,FilterView):
    paginate_by = 10
    model = Provider
    template_name = 'providers/providers/index.html'
    table_class = ProviderTable
    filterset_class = ProviderFilter
    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        qs = qs.order_by("designation") 
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class ProviderDetails(DetailView):
    model = Provider
    template_name = 'providers/providers/details.html'
    
    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data()
        context['goods_provided'] = [str(x) for x in object.goods.through.objects.filter(provider = self.get_object())]
        context['services_provided'] = [str(x) for x in object.services.through.objects.filter(provider = self.get_object())]
        context['works_provided'] = [str(x) for x in object.works.through.objects.filter(provider = self.get_object())]
        context['goods_cities'] = serialize('json', object.covered_cities_Goods.all(), fields=['pk', 'longitude', 'latitude','name']) 
        context['works_cities'] = serialize('json', object.covered_cities_works.all(), fields=['pk', 'longitude', 'latitude','name'])
        context['services_cities'] = serialize('json', object.covered_cities_services.all(), fields=['pk', 'longitude', 'latitude','name'])
        context['cities_services'] = [x.name for x in object.covered_cities_services.all()]
        context['cities_goods'] = [x.name for x in object.covered_cities_Goods.all()]
        context['cities_works'] =  [x.name for x in object.covered_cities_works.all()]
    
        return context

class ProviderUpdate(UpdateView):
    model = Provider
    template_name = 'providers/providers/form.html'
    form_class = ProviderForm



class ProviderCreate(CreateView):
    model = Provider
    template_name = 'providers/providers/form.html'
    form_class = ProviderForm


class ProviderDelete(DeleteView):
    model = Provider
    success_url = reverse_lazy('providers-list')
    
    def form_valid(self, form):
        messages.success(self.request, _("The provider was delete successfully"))
        return super().form_valid(form)

#Services views    
class ServicesList(SingleTableMixin,FilterView):
    paginate_by = 10
    model = Service
    template_name = 'providers/services/index.html'
    table_class = ServicesTable
    filterset_class = ServiceFilter
    def get_queryset(self, *args, **kwargs): 
        qs = super(ServicesList, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("name") 
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(ServicesList, self).get_context_data(**kwargs)
        return context 

class ServiceDetails(DetailView):
    model = Service
    template_name = 'providers/services/details.html'
    
    def get_context_data(self, **kwargs):
        context = super(ServiceDetails, self).get_context_data()

        return context

class ServiceUpdate(UpdateView):
    model = Service
    template_name = 'providers/services/form.html'
    form_class = ServiceForm

class ServiceCreate(CreateView):
    model = Service
    template_name = 'providers/services/form.html'
    form_class = ServiceForm

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services-list')
    
    def form_valid(self, form):
        messages.success(self.request, _("The service was delete successfully"))
        return super(ServiceDelete,self).form_valid(form)

class GoodsList(SingleTableMixin,FilterView):
    paginate_by = 10
    model = Good
    template_name = 'providers/goods/index.html'
    table_class = GoodsTable
    filterset_class = GoodFilter
    def get_queryset(self, *args, **kwargs): 
        qs = super(GoodsList, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("name") 
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class GoodDetails(DetailView):
    model = Good
    template_name = 'providers/goods/details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context

class GoodUpdate(UpdateView):
    model = Good
    template_name = 'providers/goods/form.html'
    form_class = GoodForm

class GoodCreate(CreateView):
    model = Good
    template_name = 'providers/goods/form.html'
    form_class = GoodForm

class GoodDelete(DeleteView):
    model = Good
    success_url = reverse_lazy('goods-list')
    
    def form_valid(self, form):
        messages.success(self.request, _("The good was delete successfully"))
        return super().form_valid(form)

class WorksList(SingleTableMixin,FilterView):
    paginate_by = 10
    model = Work
    template_name = 'providers/works/index.html'
    table_class = WorksTable
    filterset_class = WorkFilter
    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        qs = qs.order_by("name") 
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    
class WorkDetails(DetailView):
    model = Work
    template_name = 'providers/works/details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

class WorkUpdate(UpdateView):
    model = Work
    template_name = 'providers/works/form.html'
    form_class = WorkForm

class WorkCreate(CreateView):
    model = Work
    template_name = 'providers/works/form.html'
    form_class = WorkForm

class WorkDelete(DeleteView):
    model = Work
    success_url = reverse_lazy('works-list')
    
    def form_valid(self, form):
        messages.success(self.request, _("The work was delete successfully"))
        return super().form_valid(form)
    
class EvaluationCreate(CreateView):
    model = Work
    template_name = 'providers/evaluations/form.html'
    form_class = EvaluationForm

class EvaluationCreate(UpdateView):
    model = Work
    template_name = 'providers/evaluations/form.html'
    form_class = EvaluationForm



