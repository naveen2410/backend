from django.contrib import admin
from .models import Qaconnconfig # add this

class QaconnconfigAdmin(admin.ModelAdmin):  # add this
    list_display = ('qaconnid', 'systemtype', 'ipaddress', 'port', 'adminuser', 'adminpass', 'sysid', 'client', 'githuburl', 'triggerrate', 'triggeruom')

# Register your models here.
admin.site.register(Qaconnconfig, QaconnconfigAdmin) # add this