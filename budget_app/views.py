from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Transaction, Entry
from .forms import EntryForm
# Create your views here.
def index(request):
    return render(request, 'budget_app/index.html')

def transactions(request):
    transactions = Transaction.objects.order_by('date_added')
    context = {"transactions" : transactions}
    return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    entries = transaction.entry_set.order_by('-date_added')
    context = {'transaction': transaction, 'entries': entries}
    return render(request, 'budget_app/transaction.html', context)

def new_entry(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.transaction = transaction
            new_entry.save()
            return HttpResponseRedirect(reverse('budget_app:transaction', args=[transaction_id]))
    context = {'transaction': transaction, 'form': form}
    return render(request, 'budget_app/new_entry.html', context)

def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    return redirect('budget_app:transactions')
