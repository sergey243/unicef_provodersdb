from django.utils.safestring import mark_safe
from django_tables2 import tables
from django.utils.translation import gettext as _
from cities_light.models import City

class CitiesTable(tables.Table) :
    name = tables.columns.Column(accessor="name",verbose_name=_('name'))
    region = tables.columns.Column(accessor="region",verbose_name=_('region'))
    count = tables.columns.Column(verbose_name=_('Count'),accessor='providers__count')
    
    class Meta:
        model = City
        template_name = "table.html"
        fields = ('name',"region")
