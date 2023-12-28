from  django import forms
from .models import Provider, Service, Good, Work

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ("designation", "responsible", "contacts", "phone",
                    "email","website",'city','address','works','goods','services',
                    'subsidiaries','tax_id','rccm','national_id','bank_domiciliation',
                    'active_since','ungm_number','unicef_vendor_number',
                    'is_manifactor','is_importer','goods_orgin','is_retailer','is_wholeseller',
                    'annual_turnover_crncy','last_turnover','past_annual_turnover',
                    'employees_count','is_accredited_provider','partners',
                    'workspaces','equipments','competition','affiliations','affiliate_to_commerce_chamber',
                    'reason_no_affiliate','offers_previously_provided','selection_mode',
                    'advantages','covered_cities_Goods','covered_cities_works',
                    'covered_cities_services','comment')
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("name", "description")

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ("name", "description")

class WorkForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("name", "description")

        