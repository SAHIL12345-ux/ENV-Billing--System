from django import forms # type: ignore
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name','invoice_number','amount','is_paid','notes']
                  