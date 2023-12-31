# Generated by Django 4.2.8 on 2023-12-13 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                ("modified_at", models.DateTimeField(editable=False)),
                (
                    "name",
                    models.CharField(max_length=500, unique=True, verbose_name="name"),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[("G", "Goods"), ("S", "Services"), ("W", "Works")],
                        max_length=1,
                        verbose_name="category",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ocreator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_modify_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="omodifier",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "offers",
                "db_table_comment": "Services, works and goods required by Unicef",
                "ordering": ["name"],
                "get_latest_by": ["created_at", "modified_at"],
                "default_related_name": "offers",
            },
        ),
        migrations.CreateModel(
            name="OffersProvided",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="comment"
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cities_light.city",
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="providers.offer",
                    ),
                ),
            ],
            options={
                "db_table": "offers_provided",
                "db_table_comment": "Offers actually provided by the providers retained by Unicef per city",
                "get_latest_by": ["created_at"],
                "default_related_name": "offers_provided",
            },
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                ("modified_at", models.DateTimeField(editable=False)),
                (
                    "designation",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="designation"
                    ),
                ),
                (
                    "responsible",
                    models.CharField(max_length=250, verbose_name="responsible"),
                ),
                (
                    "contacts",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="contacts"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="phone"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=150, null=True, verbose_name="email"
                    ),
                ),
                (
                    "website",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="website"
                    ),
                ),
                ("address", models.CharField(max_length=250, verbose_name="address")),
                (
                    "subsidiaries",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="subsidiaries",
                    ),
                ),
                ("tax_id", models.CharField(max_length=15, verbose_name="tax id")),
                ("rccm", models.CharField(max_length=15, verbose_name="R.C.C.M")),
                (
                    "national_id",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="national ID"
                    ),
                ),
                (
                    "bank_domiciliation",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="bank domiciliation",
                    ),
                ),
                (
                    "active_since",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="active since"
                    ),
                ),
                (
                    "ungm_number",
                    models.CharField(
                        blank=True, max_length=25, null=True, verbose_name="UNGM number"
                    ),
                ),
                (
                    "unicef_vendor_number",
                    models.CharField(
                        blank=True,
                        max_length=25,
                        null=True,
                        verbose_name="unicef vendo ID",
                    ),
                ),
                (
                    "is_manifactor",
                    models.BooleanField(default=False, verbose_name="is manifactor"),
                ),
                (
                    "is_importer",
                    models.BooleanField(default=False, verbose_name="is importer"),
                ),
                (
                    "is_retailer",
                    models.BooleanField(default=False, verbose_name="is retailer"),
                ),
                (
                    "is_wholeseller",
                    models.BooleanField(default=False, verbose_name="is wholeseller"),
                ),
                (
                    "annual_turnover_crncy",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("USD", "US Dollars"),
                            ("CDF", "Congolese franc"),
                            ("CFA", "Central African CFA franc"),
                            ("TZS", "Tanzanian shilling"),
                            ("AOA", "Angolan kwanza"),
                            ("UGX", "Ugandan Shillings"),
                            ("BIF", "Burundian franc"),
                            ("ZMW", "Congolese franc"),
                            ("CDF", "Zambian kwacha"),
                        ],
                        default="USD",
                        max_length=4,
                        null=True,
                        verbose_name="annual turnover currency",
                    ),
                ),
                (
                    "last_turnover",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="previous annual turnover",
                    ),
                ),
                (
                    "past_annual_turnover",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="2 years back annual turnover",
                    ),
                ),
                (
                    "employees_count",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="number of full time employees",
                    ),
                ),
                (
                    "is_accredited_provider",
                    models.BooleanField(
                        default=False, verbose_name="is acrredited provider"
                    ),
                ),
                (
                    "partners",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="partners"
                    ),
                ),
                (
                    "workspaces",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="workspace"
                    ),
                ),
                (
                    "equipments",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="equipments"
                    ),
                ),
                (
                    "competition",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="competition",
                    ),
                ),
                (
                    "affiliations",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="affiliations",
                    ),
                ),
                (
                    "affiliate_to_commerce_chamber",
                    models.BooleanField(
                        default=False, verbose_name="is member of the commerce chamber"
                    ),
                ),
                (
                    "reason_no_affiliate",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="reason for not being member of commerce chamber",
                    ),
                ),
                (
                    "offers_previously_provided",
                    models.CharField(
                        blank=True,
                        help_text="ordres received from Unicef, other united state organizations, bilateral coperation agencies or gorvenemental agencies fro the pqst three year",
                        max_length=500,
                        null=True,
                        verbose_name="offers previously provided",
                    ),
                ),
                (
                    "selection_mode",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("tender", "on tender call"),
                            ("consultation", "restricted consultation"),
                            ("excusive", "on direct order"),
                        ],
                        default="tender",
                        max_length=50,
                        null=True,
                        verbose_name="mode of selection",
                    ),
                ),
                (
                    "advantages",
                    models.CharField(
                        blank=True,
                        max_length=350,
                        null=True,
                        verbose_name="proposed advantages",
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="comment"
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cities_light.city",
                        verbose_name="city",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="country",
                        to="cities_light.country",
                        verbose_name="country",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pcreator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "goods_orgin",
                    models.ManyToManyField(
                        related_name="origins",
                        to="cities_light.country",
                        verbose_name="origin of goods",
                    ),
                ),
                (
                    "last_modify_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pmodifier",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offers",
                    models.ManyToManyField(
                        through="providers.OffersProvided", to="providers.offer"
                    ),
                ),
            ],
            options={
                "db_table": "providers",
                "db_table_comment": "Provider identified and retained by Unicef",
                "ordering": ["designation"],
                "get_latest_by": ["created_at", "modified_at"],
                "default_related_name": "providers",
            },
        ),
        migrations.AddField(
            model_name="offersprovided",
            name="provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="providers.provider"
            ),
        ),
    ]
