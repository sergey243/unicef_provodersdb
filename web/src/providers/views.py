import csv
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from djqscsv import render_to_csv_response
from django.db.models.base import Model as Model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, View, ListView
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.utils.translation import gettext_lazy as _
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
import pandas as pd
from io import BytesIO
from .models import Provider, Service, Work, Good, Evaluation
from .tables import ProviderTable, ServicesTable, WorksTable, GoodsTable, EvaluationTable
from .filters import ProviderFilter, ServiceFilter, GoodFilter, WorkFilter
from .forms import ProviderForm,ServiceForm, GoodForm, WorkForm, EvaluationForm, BulkDeleteForm


class ProviderExport(SingleTableMixin,FilterView,ListView,PermissionRequiredMixin):
    permission_required = ("providers.provider.can_view_provider")
    model = Provider
    filterset_class = ProviderFilter
    template_name = 'providers/providers/export.html'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.values('designation','responsible','contacts','phone','email','website',
                  'city__name','address','subsidiaries','tax_id','rccm','national_id','bank_domiciliation',
                  'active_since','ungm_number','unicef_vendor_number','is_manifactor','is_importer',
                  'is_retailer','is_wholeseller','annual_turnover_crncy','last_turnover','past_annual_turnover',
                  'employees_count','is_accredited_provider','goods_orgin','partners','workspaces',
                  'equipments','competition','affiliations','affiliate_to_commerce_chamber',
                  'reason_no_affiliate','offers_previously_provided','selection_mode','advantages',
                  'comment')
    def post(self, request, *args, **kwargs)-> HttpResponse:

        f = ProviderFilter(request.POST,queryset=self.get_queryset())

        if(f.is_valid()):

            df = pd.DataFrame(list(f.qs.values('designation','responsible','contacts','phone','email','website',
                    'city__name','address','subsidiaries','tax_id','rccm','national_id','bank_domiciliation',
                    'active_since','ungm_number','unicef_vendor_number','is_manifactor','is_importer',
                    'is_retailer','is_wholeseller','annual_turnover_crncy','last_turnover','past_annual_turnover',
                    'employees_count','is_accredited_provider','goods_orgin','partners','workspaces',
                    'equipments','competition','affiliations','affiliate_to_commerce_chamber',
                    'reason_no_affiliate','offers_previously_provided','selection_mode','advantages',
                    'comment')))
            print(df.shape)
            with BytesIO() as b:
                # Use the StringIO object as the filehandle.
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Sheet1')
                writer.close()
                filename = 'providers'
                content_type = 'application/vnd.ms-excel'
                response = HttpResponse(b.getvalue(), content_type=content_type)
                response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
                return response
        context = dict()
        context['filter'] = f
        return render(request,self.template_name,context)
        



#Providers views
class ProvidersList(PermissionRequiredMixin,SingleTableMixin,FilterView):
    permission_required = ("providers.provider.can_view_provider")
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

class ProviderDetails(DetailView, SingleTableMixin):
    model = Provider
    template_name = 'providers/providers/details.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        qs = qs.order_by("-created_at") 
        return qs
    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super().get_context_data()
        page = self.request.GET.get("page", 1)
        context['goods_provided'] = [str(x) for x in object.goods.through.objects.filter(provider = self.get_object())]
        context['services_provided'] = [str(x) for x in object.services.through.objects.filter(provider = self.get_object())]
        context['works_provided'] = [str(x) for x in object.works.through.objects.filter(provider = self.get_object())]
        context['goods_cities'] = serialize('json', object.covered_cities_Goods.all(), fields=['pk', 'longitude', 'latitude','name']) 
        context['works_cities'] = serialize('json', object.covered_cities_works.all(), fields=['pk', 'longitude', 'latitude','name'])
        context['services_cities'] = serialize('json', object.covered_cities_services.all(), fields=['pk', 'longitude', 'latitude','name'])
        context['cities_services'] = [x.name for x in object.covered_cities_services.all()]
        context['cities_goods'] = [x.name for x in object.covered_cities_Goods.all()]
        context['cities_works'] =  [x.name for x in object.covered_cities_works.all()]
        context['table'] = EvaluationTable(Evaluation.objects.filter(provider=object))
        context['table'].paginate(page=self.request.GET.get("page", 1), per_page=10) 
    
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

def providers_delete(request):
    if request.method == 'POST':
        ids = request.POST.get("ids", [])
        form = BulkDeleteForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            _selection = list()
            try:
                for id in selection:
                    _selection.append(int(id))
                Provider.objects.filter(pk__in=_selection).delete()
            except Exception as e:
                pass
            
    return redirect('providers-list')

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
    
def services_delete(request):
    if request.method == 'POST':
        ids = request.POST.get("ids", [])
        form = BulkDeleteForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            _selection = list()
            try:
                for id in selection:
                    _selection.append(int(id))
                Service.objects.filter(pk__in=_selection).delete()
            except Exception as e:
                pass
            
    return redirect('services-list')

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

def goods_delete(request):
    if request.method == 'POST':
        ids = request.POST.get("ids", [])
        form = BulkDeleteForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            _selection = list()
            try:
                for id in selection:
                    _selection.append(int(id))
                Good.objects.filter(pk__in=_selection).delete()
            except Exception as e:
                pass
            
    return redirect('goods-list')

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
    
def works_delete(request):
    if request.method == 'POST':
        ids = request.POST.get("ids", [])
        form = BulkDeleteForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            _selection = list()
            try:
                for id in selection:
                    _selection.append(int(id))
                Work.objects.filter(pk__in=_selection).delete()
            except Exception as e:
                pass
            
    return redirect('works-list')
    
class EvaluationCreate(CreateView):
    model = Evaluation
    template_name = 'providers/evaluations/form.html'
    form_class = EvaluationForm

    def get(self, request, pk, *args, **kwargs):
        provider = get_object_or_404(Provider,pk=pk)
        self.initial["provider"] = provider
        form = self.form_class(initial=self.initial)
        form.fields['goods'].queryset = provider.goods.all()
        form.fields['works'].queryset = provider.works.all()
        form.fields['services'].queryset = provider.services.all()
        self.success_url = reverse('provider-details', kwargs={'pk': provider.pk})
        return render(request,self.template_name,{'form':form, 'provider':provider})
    def post(self, request: HttpRequest, pk:int,*args: str, **kwargs: Any) -> HttpResponse:
        form = EvaluationForm(request.POST)
        context = dict()
        provider = get_object_or_404(Provider,pk=pk)
        form.initial["provider"] = provider.pk
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.created_by = request.user
            evaluation.provider = provider
            evaluation.save()
            return HttpResponseRedirect(reverse_lazy('provider-details', args=[provider.pk]))
        form.fields['goods'].queryset = provider.goods.all()
        form.fields['works'].queryset = provider.works.all()
        form.fields['services'].queryset = provider.services.all()
        context["provider"] = provider
        context["form"] = form
        return render(request, self.template_name, context)



class EvaluationUpdate(UpdateView):
    model = Evaluation
    template_name = 'providers/evaluations/form.html'
    form_class = EvaluationForm

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        user = request.user
        evaluation = self.get_object()
        form = EvaluationForm(instance=evaluation)
        form.fields['goods'].queryset = evaluation.provider.goods.all()
        form.fields['works'].queryset = evaluation.provider.works.all()
        form.fields['services'].queryset = evaluation.provider.services.all()
        context["form"] = form
        context["object"] = evaluation
        context["provider"] = evaluation.provider
        context["creator"] = user.get_username()
        return render(request,self.template_name,context)
        
    
    def post(self, request: HttpRequest, pk:int, *args: str, **kwargs: Any) -> HttpResponse:
        context = dict()
        user = request.user
        evaluation = get_object_or_404(Evaluation,pk=pk)
        form = EvaluationForm(request.POST,instance=evaluation)
        provider = get_object_or_404(Provider,pk=request.POST["provider"])
        if form.is_valid():
            _evaluation = form.save()
            _evaluation.last_modify_by = user            
            _evaluation.save()
            return HttpResponseRedirect(reverse_lazy('provider-details', args=[provider.pk]))
        form.fields['goods'].queryset = provider.goods.all()
        form.fields['works'].queryset = provider.works.all()
        form.fields['services'].queryset = provider.services.all()
        context["form"] = form
        context["provider"] = provider
        context["object"] = evaluation
        context["creator"] = user.get_username()
        return render(request, self.template_name, context)


class EvaluationDelete(DeleteView):
    model = Evaluation

    def form_valid(self, form):
        self.success_url = reverse_lazy('provider-details',kwargs={'pk': self.get_object().provider.pk})
        messages.success(self.request, _("The evaluation was delete successfully"))
        return super().form_valid(form)






