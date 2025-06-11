from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('sum', 'person', 'payment_type', 'currency', 'currency_type', 'FactOrPlanned', 'TakeIntoReports', 'payment_date', 'description')

