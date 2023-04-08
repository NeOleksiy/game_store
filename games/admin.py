from django.contrib import admin
from games.models import Category, Products, PurchaseMethod, Slider, purchase, Publisher, Developer, Basket

from users.models import Users, EmailVerification

# Register your models here.


admin.site.register(Category)
admin.site.register(PurchaseMethod)
admin.site.register(Slider)
admin.site.register(Users)
admin.site.register(purchase)
admin.site.register(Publisher)
admin.site.register(Developer)
admin.site.register(Basket)
admin.site.register(EmailVerification)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    fields = ()
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'timestamp')
    readonly_fields = ('timestamp',)
    extra = 0
