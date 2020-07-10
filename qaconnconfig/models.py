from django.db import models
    # Create your models here.

    # add this
class Qaconnconfig(models.Model):
    
    #systemname = models.CharField(max_length=10)
    #systemendpoint = models.CharField(max_length=10)
    #user = models.CharField(max_length=10)
    #password = models.CharField(max_length=10)

    qaconnid = models.CharField(max_length=50)
    systemtype = models.CharField(max_length=10)
    ipaddress = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
    adminuser = models.CharField(max_length=25)
    adminpass = models.CharField(max_length=30)
    sysid = models.CharField(max_length=2)
    client = models.CharField(max_length=3)
    githuburl = models.CharField(max_length=100)
    triggerrate = models.CharField(max_length=3)
    triggeruom = models.CharField(max_length=10)


    def _str_(self):
        return self.qaconnid