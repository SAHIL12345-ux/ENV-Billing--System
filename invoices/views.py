from django.shortcuts import render,redirect ,get_object_or_404 # type: ignore

from .forms import InvoiceForm # pyright: ignore[reportMissingModuleSource]
from .models import Invoice
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'invoices/home.html')


def invoice_list(request):
    invoices = Invoice.objects.all()

    return render(
        request,
        'invoices/invoice_list.html',
        {'invoices': invoices}
    )
 

    
def create_invoice(request):
    
 if  request.method == 'POST':
    form = InvoiceForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('invoice_list')
 
 else: 
    form = InvoiceForm()
    
 return render(
        request,
        'invoices/invoice_form.html',
        {'form': form}
     
 )
     
def invoice_update(request, id):
    invoices =  get_object_or_404(Invoice, id=id)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoices)

        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoices)
        return render(
        request,
        'invoices/invoice_form.html',
        {'form': form}
    )
    
def invoice_delete(request, id):
    invoices = get_object_or_404(Invoice, id=id)
    if request.method == 'POST':
        invoices.delete()
        return redirect('invoice_list')
    
    return render(request,
    'invoices/invoice_confirm_delete.html',
    {'invoices': invoices}
    )  
def invoice_update(request, id):

    invoice = get_object_or_404(
        Invoice,
        id=id
    )

    if request.method == 'POST':

        form = InvoiceForm(
            request.POST,
            instance=invoice
        )

        if form.is_valid():

            form.save()

            return redirect('invoice_list')

    else:

        form = InvoiceForm(
            instance=invoice
        )

    return render(
        request,
        'invoices/invoice_form.html',
        {'form': form}
    )
        
        
    