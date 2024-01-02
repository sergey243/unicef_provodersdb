from  django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, MultiField, Row, Column
from .models import Provider, Service, Good, Work, Evaluation

class ProviderFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        model = Work
        fields = ("name", "description")

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ("provider","services","works","goods","lta","po_number","po_amount","description",
                    "fiability","timing","best_value","tech_specification","comment")

        