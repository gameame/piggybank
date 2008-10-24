from django.db import models
from django.contrib.auth.models import User

    
class Currency(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 5)
    simbol = models.CharField(max_length = 2)
    change_to_euro = models.DecimalField(max_digits = 10, decimal_places=2)
    
    def __unicode__(self):
        return self.name
    
class MyPiggy(models.Model):
    user = models.ForeignKey(User)
    deposit = models.DecimalField(max_digits = 10, decimal_places=2)
    target = models.DecimalField(max_digits = 10, decimal_places=2)
    default_currency = models.ForeignKey(Currency)
    cause = models.TextField()
    deadline = models.DateField()
    image = models.ImageField(upload_to = "piggys")
    default_piggy = models.ForeignKey("self", blank="True", null=True)
    
    def how_far(self):
        return "%.2f" % self.target - self.deposit
    
    def deposit_str(self):
        return "%.2f %s (%.2f %s)" % (self.deposit, self.default_currency.simbol,
                                      self.target, self.default_currency.simbol)
    deposit_str.short_description = "deposit (target)"
    
    def __unicode__(self):
        return self.cause 

class Coin(models.Model):
    currency = models.ForeignKey(Currency)
    value = models.DecimalField(max_digits = 10, decimal_places=2)
    icon = models.ImageField(upload_to = "icons")
    
    def __unicode__(self):
        s = self.currency.name
        if self.value < 1:
            v = self.value * 100
            s = "%s cent" % s
        else:
            v = self.value
        return "%d %s" % (v, s)