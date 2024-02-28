from django.db import models
from django.db.models import fields, Model, Q
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from cities_light import models as cities_models
from multiselectfield import MultiSelectField
from django.urls import reverse

OFFERS = (
    ('G', _('Goods')),
    ('S',_('Services')),
    ('W',_('Works')),
)

CURRENCIES = (
    ('USD',_('US Dollars')),
    ('CDF',_('Congolese franc')),
    ('CFA',_('Central African CFA franc')),
    ('TZS',_('Tanzanian shilling')),
    ('AOA',_('Angolan kwanza')),
    ('UGX',_('Ugandan Shillings')),
    ('BIF',_('Burundian franc')),
    ('ZMW',_('Congolese franc')),
    ('CDF',_('Zambian kwacha')),
)

SELECTION_MODE = (
    ('tender',_('On tender call')),
    ('consultation',_('Restricted consultation')),
    ('excusive',_('On direct order'))
)

ADVANTAGES = (
    ('after sales service',_('After sales service')),
    ('discounts/rebates',_('Discounts/rebates')),
    ('on-site deliveries',_('On-site deliveries'))
)

EVALUATION = (
    (1,_('poor')),
    (2,_('not satisfying')),
    (3,_('acceptable')),
    (4,_('good')),
    (5,_('excelent'))
)

EVALUATION_CONCLUSION = (
    (0, _("Yes, we can keep working with this provider.")),
    (1, _("No, we should not be working with this provider anymore."))
)

class Site(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="site_creator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="site_modifier",null=True,blank=True,on_delete=models.PROTECT)
    name = models.CharField(verbose_name=_('name'),unique=True,blank=False,null=False,max_length=150)
    city = models.ForeignKey('cities_light.City',verbose_name= _('city'), on_delete=models.SET_NULL, null=True, blank=True)
    address = fields.TextField(verbose_name=_("description"),editable=True,max_length=250,null=True,blank=True)
    description = fields.TextField(verbose_name=_("description"),editable=True,max_length=500,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Site,self).save(*args,**kwargs)

    class Meta:
        db_table_comment = "Work sites of Unicef"
        default_related_name = "sites"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["name"]
        db_table = "sites"

class Work(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="wcreator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="wmodifier",null=True,blank=True,on_delete=models.PROTECT)
    name = fields.CharField(verbose_name=_("name"),editable=True,unique=True,max_length=500,null=False,blank=False)      
    description = fields.TextField(verbose_name=_("description"),editable=True,max_length=500,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Work,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('work-details',args=[self.pk])   
    class Meta:
        db_table_comment = "Works required by Unicef"
        default_related_name = "works"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["name"]
        db_table = "works"

class Service(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="screator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="smodifier",null=True,blank=True,on_delete=models.PROTECT)
    name = fields.CharField(verbose_name=_("name"),editable=True,unique=True,max_length=500,null=False,blank=False)      
    description = fields.TextField(verbose_name=_("description"),editable=True,max_length=500,null=True,blank=True)
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Service,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('service-details',args=[self.pk])
    
    class Meta:
        db_table_comment = "Services required by Unicef"
        default_related_name = "services"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["name"]
        db_table = "services"

class Good(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="gcreator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="gmodifier",null=True,blank=True,on_delete=models.PROTECT)
    name = fields.CharField(verbose_name=_("name"),editable=True,unique=True,max_length=500,null=False,blank=False)      
    description = fields.TextField(verbose_name=_("description"),editable=True,max_length=500,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Good,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('good-details',args=[self.pk])
    
    class Meta:
        db_table_comment = "Goods required by Unicef"
        default_related_name = "goods"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["name"]
        db_table = "goods"
        

class ServicesProvided(models.Model):
    provider = models.ForeignKey('Provider',related_name="service_provider", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        return super(ServicesProvided,self).save(*args,**kwargs) 
    
    def __str__(self):
        return self.service.name
    class Meta:
        db_table_comment = "Services actually provided by the providers retained by Unicef per city"
        default_related_name = "services_provided"
        get_latest_by = ["created_at"]
        get_latest_by = ["created_at"]
        db_table = "services_provided"
        unique_together = ('provider', 'service')

class GoodsProvided(models.Model):
    provider = models.ForeignKey('Provider',related_name="goods_provider", on_delete=models.CASCADE)
    goods = models.ForeignKey(Good, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        return super(GoodsProvided,self).save(*args,**kwargs) 
    def __str__(self):
        return self.goods.name
    class Meta:
        db_table_comment = "Goods actually provided by the providers retained by Unicef per city"
        default_related_name = "goods_provided"
        get_latest_by = ["created_at"]
        get_latest_by = ["created_at"]
        db_table = "goods_provided"
        unique_together = ('provider', 'goods')

class WorkExecuted(models.Model):
    provider = models.ForeignKey('Provider',related_name="contractor", on_delete=models.CASCADE)
    works = models.ForeignKey(Work,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        return super(WorkExecuted,self).save(*args,**kwargs) 

    def __str__(self):
        return self.works.name
    class Meta:
        default_related_name = "works_executed"
        get_latest_by = ["created_at"]
        get_latest_by = ["created_at"]
        db_table = "works_executed"
        unique_together = ('provider', 'works')

class Provider(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="pcreator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="pmodifier",null=True,blank=True,on_delete=models.PROTECT)
    designation = fields.CharField(verbose_name=_("designation"),unique=True,max_length=250,null=False,blank=False)
    responsible = fields.CharField(verbose_name=_("responsible"),max_length=250,null=False,blank=False)
    works = models.ManyToManyField(Work,verbose_name=_("works executed"),through=WorkExecuted,editable=True,blank=True)
    services = models.ManyToManyField(Service,verbose_name=_("services provided"),through=ServicesProvided,editable=True,blank=True)
    goods = models.ManyToManyField(Good,verbose_name=_("good provided"),through=GoodsProvided,editable=True,blank=True)
    contacts = fields.TextField(verbose_name=_("contacts"),max_length=500,null=True,blank=True)
    phone = fields.CharField(verbose_name=_("phone"),max_length=150,null=True,blank=True)
    email = fields.EmailField(verbose_name=_("email"),max_length=150,null=True,blank=True)
    website = fields.CharField(verbose_name=_("website"),max_length=500,null=True,blank=True)
    country = models.ForeignKey('cities_light.Country',verbose_name= _('country'),on_delete=models.SET_NULL, null=True, blank=True,related_name="country") 
    city = models.ForeignKey('cities_light.City',verbose_name= _('city'), on_delete=models.SET_NULL, null=True, blank=True)
    address = fields.TextField(verbose_name=_("address"),max_length=500,null=False,blank=False)
    subsidiaries = fields.CharField(verbose_name=_("subsidiaries"),max_length=500, blank=True, null=True)
    tax_id = fields.CharField(verbose_name=_("tax id"),max_length=50, blank=False, null=True)
    rccm = fields.CharField(verbose_name=_("R.C.C.M"),max_length=50, blank=False, null=True)
    national_id = fields.CharField(verbose_name=_("national ID"),max_length=150, blank=True, null=True)
    bank_domiciliation = fields.CharField(verbose_name=_("bank domiciliation"),max_length=50, blank=True, null=True)
    active_since = fields.IntegerField(verbose_name=_("active since"), blank=True, null=True)
    ungm_number = fields.CharField(verbose_name=_("UNGM number"),max_length=150, blank=True, null=True)
    unicef_vendor_number = fields.CharField(verbose_name=_("unicef vendo ID"),max_length=150, blank=True, null=True)
    is_manifactor = fields.BooleanField(verbose_name=_("is manifactor"),default=False,blank=False,null=False)
    is_importer = fields.BooleanField(verbose_name=_("is importer"),default=False,blank=False,null=False)
    is_retailer = fields.BooleanField(verbose_name=_("is retailer"),default=False,blank=False,null=False)
    is_wholeseller = fields.BooleanField(verbose_name=_("is wholeseller"),default=False,blank=False,null=False)
    annual_turnover_crncy = fields.CharField(verbose_name=_("annual turnover currency"),max_length=4, blank=True, null=True,choices=CURRENCIES, default='USD')
    last_turnover = fields.CharField(verbose_name=_("previous annual turnover"),max_length=30, blank=True, null=True)
    past_annual_turnover = fields.CharField(verbose_name=_("2 years back annual turnover"),max_length=30, blank=True, null=True)
    employees_count = fields.CharField(verbose_name=_("number of full time employees"),max_length=150, blank=True, null=True)
    is_accredited_provider = fields.BooleanField(verbose_name=_("is acrredited provider"),default=False,blank=False,null=False)
    goods_orgin = fields.CharField(verbose_name=_('origin of goods'), max_length=250,blank=True,null=True)
    partners = fields.CharField(verbose_name=_("partners"),max_length=500, blank=True, null=True)
    workspaces = fields.CharField(verbose_name=_("workspace"),max_length=500, blank=True, null=True)
    equipments = fields.TextField(verbose_name=_("equipments"),max_length=500, blank=True, null=True)
    competition = fields.TextField(verbose_name=_("competition"),max_length=500, blank=True, null=True)
    affiliations = fields.TextField(verbose_name=_("affiliations"),max_length=500, blank=True, null=True)
    affiliate_to_commerce_chamber = fields.BooleanField(verbose_name=_("is member of the commerce chamber"),default=False, blank=False, null=False)
    reason_no_affiliate = fields.CharField(verbose_name=_("reason for not being member of commerce chamber"),max_length=500, blank=True, null=True)
    offers_previously_provided = fields.CharField(verbose_name=_("offers previously provided"),max_length=500, blank=True, null=True,
                                                  help_text=_("ordres received from Unicef, other united state organizations, bilateral coperation agencies or gorvenemental agencies fro the pqst three year"))
    selection_mode = fields.CharField(verbose_name=_("mode of selection"),max_length=50, blank=True, null=True,choices=SELECTION_MODE, default='tender')
    advantages = MultiSelectField(verbose_name=_("proposed advantages"),choices=ADVANTAGES, blank=True, null=True,max_choices=3, max_length=2048)
    covered_cities_Goods = models.ManyToManyField(cities_models.City, related_name="covered_cities_goods",verbose_name=_('covered cities for goods'),blank=True)
    covered_cities_works = models.ManyToManyField(cities_models.City, related_name="covered_cities_works",verbose_name=_('covered cities for works'),blank=True)
    covered_cities_services = models.ManyToManyField(cities_models.City, related_name="covered_cities_services",verbose_name=_('covered cities for services'),blank=True)
    comment = fields.TextField(verbose_name=_("comment"),max_length=500,null=True,blank=True)

    @property
    def is_contractor(self):
        return WorkExecuted.objects.filter(provider= self ).exists()
    
    @property
    def is_service_provider(self):
        return ServicesProvided.objects.filter(provider= self ).exists()

    @property
    def is_good_provider(self):
        return GoodsProvided.objects.filter(provider= self ).exists()
    
    def clean(self):
        from django.core.exceptions import ValidationError
        duplicate = Provider.objects.filter(models.Q(unicef_vendor_number= self.unicef_vendor_number)|models.Q(ungm_number= self.ungm_number))
        if duplicate.exists() and not self.pk:
            raise ValidationError(_('A provider with the same vendor number or Unicef number exist.'))


    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Provider,self).save(*args,**kwargs)

    def __str__(self):
        return self.designation

    def get_absolute_url(self):
        return reverse('provider-details',args=[self.pk])
    class Meta:
        db_table_comment = "Provider identified and retained by Unicef"
        default_related_name = "providers"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["designation"]
        db_table = "providers"

class Evaluation(Model):
    created_at = fields.DateTimeField(editable=False,verbose_name=_("created at"))
    modified_at = fields.DateTimeField(editable=False,verbose_name=_("last modified at"))
    created_by = models.ForeignKey(get_user_model(),editable=False,related_name="ecreator",null=True,blank=True,on_delete=models.PROTECT)
    last_modify_by = models.ForeignKey(get_user_model(),editable=False,related_name="emodifier",null=True,blank=True,on_delete=models.PROTECT)
    provider = models.ForeignKey('Provider',related_name="provider", on_delete=models.CASCADE, verbose_name=_('provider'))
    site = models.ForeignKey('Site',verbose_name=_("site"),on_delete=models.CASCADE,blank=False,null=False)
    period_start = models.DateField(verbose_name=_('period start'),blank=False,null=False)
    period_end = models.DateField(verbose_name=_('period end'),blank=False,null=False)
    works = models.ManyToManyField(Work,verbose_name=_("works evaluated"),editable=True,blank=True)
    services = models.ManyToManyField(Service,verbose_name=_("services evaluated"),editable=True,blank=True)
    goods = models.ManyToManyField(Good,verbose_name=_("good evaluated"),editable=True,blank=True)
    lta = models.CharField(verbose_name=_('LTA number'),max_length=50,blank=False,null=False)
    po_number = models.CharField(verbose_name=_('PO number'),max_length=50,blank=False,null=False)
    po_amount = models.DecimalField(verbose_name=_('PO amount'),decimal_places=2,max_digits=20,blank=False,null=False)
    description = fields.TextField(verbose_name=_("description"),max_length=500,null=True,blank=True)
    fiability = fields.IntegerField(verbose_name=_('fiability'),choices=EVALUATION,blank=False, null=False)
    timing = fields.IntegerField(verbose_name=_('timing'),choices=EVALUATION,blank=False, null=False)
    best_value = fields.IntegerField(verbose_name=_('quality-price report'),choices=EVALUATION,blank=False, null=False)
    tech_specification = fields.IntegerField(verbose_name=_('technical specifications'),choices=EVALUATION,blank=False, null=False)
    conclusion = models.IntegerField(verbose_name=_("conclusion"),choices=EVALUATION_CONCLUSION,blank=False,null=False)
    comment = fields.TextField(verbose_name=_("comment"),max_length=500,null=True,blank=True)

    @property
    def performance(self):
        _performance = self.fiability + self.timing + self.best_value + self.tech_specification
        if(_performance > 14): return 'A'
        elif(_performance <= 14 and _performance >= 10): return 'B'
        elif(_performance < 10 and _performance >= 3): return 'C'
        else: return 'D'
    
    def __str__(self):
        return '{}:'.format(self.pk)

    def save(self, *args, **kwargs):
        
        if not self.id:
            self.created_at = timezone.now()
        if not self.created_at:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        
        return super(Evaluation,self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('provider-details',args=[self.provider.pk])
    class Meta:
        default_related_name = "evaluations"
        get_latest_by = ["created_at","modified_at"]
        get_latest_by = ["created_at","modified_at"]
        ordering = ["provider"]
        db_table = "evaluations"
