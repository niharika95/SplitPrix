from django.db import models
import datetime

class Transaction(models.Model):
	billingDate = models.DateField(_("Date"), default=datetime.date.today)
	storeName = models.CharField(max_length=50)
	# add lists for users and dictionary