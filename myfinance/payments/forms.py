from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):

    

    class Meta:
        model = Payment
        fields = ('sum', 'person', 'payment_type', 'currency', 'currency_type', 'FactOrPlanned', 'TakeIntoReports', 'payment_date', 'description')

        widgets = {
            'payment_date': forms.DateInput(
                format='%Y-%m-%d', # Specify the desired format for display and submission
                attrs={'type': 'date'} # This renders an HTML5 date picker
            ),
        }

