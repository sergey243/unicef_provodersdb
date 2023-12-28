from django import forms
import django_filters 
from django.utils.translation import gettext as _
from cities_light.models import City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, MultiField, Row, Column
from django.db.models import Q
from .models import Provider, OFFERS, Service, Good, Work

class ProviderFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='contains',label=_('Designation'),
                                            widget=forms.widgets.TextInput(attrs={'placeholder': _('Designation should contain')}))
    cover = django_filters.MultipleChoiceFilter(label=_('Teritorial cover'),method='filter_cover')
    services = django_filters.ModelMultipleChoiceFilter(field_name='services',queryset=Service.objects.all())
    goods = django_filters.ModelMultipleChoiceFilter(field_name='goods',queryset=Good.objects.all())
    works = django_filters.ModelMultipleChoiceFilter(field_name='works',queryset=Work.objects.all())
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.filters['cover'].extra['choices'] = [(x.pk, x.name) for x in City.objects.all()]
        except (KeyError, AttributeError):
            pass
        self.helper = FormHelper()
        self.helper.layout =  Layout(
            Div(
                Div('designation', css_class='form-group col-md-12 mb-0'),
                css_class='form-row row g-4"'
            ),
            Div(
                Div('services', css_class='form-group col-md-4 mb-0'),
                Div('works', css_class='form-group col-md-4 mb-0'),
                Div('goods', css_class='form-group col-md-4 mb-0'),
                css_class='form-row row g-4"'
            ),
            Div(
                Div('cover', css_class='form-group col-md-12 mb-0'),
                css_class='form-row row g-4"'
            )

        )
        self.helper.add_input(Submit('submit', 'Submit'))
    def filter_cover(self, queryset, name, value):
        if(value):
            cities = City.objects.filter(pk__in=value)
            q = queryset.filter(Q(city__in=cities) | Q(covered_cities_Goods__in=cities) | Q(covered_cities_works__in=cities) | Q(covered_cities_services__in=cities))
        return q
    
    class Meta:
        model = Provider
        fields = {
            'designation'
        }

class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='contains',label=_('Name'),
                                            widget=forms.widgets.TextInput(attrs={'placeholder': _('Name should contain')}))
    
    class Meta:
        model = Service
        fields = {
            'name',
        }

class GoodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='contains',label=_('Name'),
                                            widget=forms.widgets.TextInput(attrs={'placeholder': _('Name should contain')}))
    
    class Meta:
        model = Good
        fields = {
            'name',
        }

class WorkFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='contains',label=_('Name'),
                                            widget=forms.widgets.TextInput(attrs={'placeholder': _('Name should contain')}))
    
    class Meta:
        model = Work
        fields = {
            'name',
        }


        