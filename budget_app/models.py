from django.db import models


    
class Transaction(models.Model):
# Create your models here.
    TransactionType = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.TransactionType)

class Entry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    merchant = models.CharField(max_length=200)
    description = models.TextField()
    transaction_amount = models.FloatField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return str(self.merchant)