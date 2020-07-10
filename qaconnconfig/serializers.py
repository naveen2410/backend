from rest_framework import serializers
from .models import Qaconnconfig

class QaconnconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qaconnconfig
        fields = ('id','qaconnid', 'systemtype', 'ipaddress', 'port', 'adminuser', 'adminpass', 'sysid', 'client', 'githuburl', 'triggerrate', 'triggeruom')