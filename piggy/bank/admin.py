from piggy.bank.models import MyPiggy
from piggy.bank.models import Currency
from piggy.bank.models import Coin
from django.contrib import admin

class MyPiggyAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "deposit_str")
    list_filter = ("user",)
    #exclude = ('user', 'deposit')
    def save_model(self, request, obj, form, change):
        obj.deposit = 0
        obj.user = request.user
        obj.save()

class CoinInline(admin.TabularInline):
    model = Coin
    extra = 3
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "change_to_euro")
    inlines = [
               CoinInline
               ]
    
class CoinAdmin(admin.ModelAdmin):
    list_filter = ("currency",)
    

admin.site.register(MyPiggy, MyPiggyAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Coin, CoinAdmin)