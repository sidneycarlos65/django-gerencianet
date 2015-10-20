from django.conf import settings
from django.contrib import admin

from gerencianet.models import PaymentLog


class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "identifier", "email", "data", "response")

    def has_add_permission(self, request):
        return False if not hasattr(settings, "ADMIN_ADD_BUTTOM") else settings.ADMIN_ADD_BUTTOM

admin.site.register(PaymentLog, PaymentLogAdmin)
