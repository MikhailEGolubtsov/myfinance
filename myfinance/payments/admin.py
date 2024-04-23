from django.contrib import admin

from .models import Currency, CurrencyType, Payment, PaymentType, Person

admin.site.register(Currency)
admin.site.register(CurrencyType)
admin.site.register(Payment)
admin.site.register(PaymentType)
admin.site.register(Person)
