from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvoicesConfig(AppConfig):
    name = 'test_invoice.invoices'
    verbose_name = _("Invoices")