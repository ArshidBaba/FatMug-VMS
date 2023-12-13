from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VendorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps_vendors"
    verbose_name = _("Vendors")