from django.db import models
from django.utils import timezone

# Create your models here.

class MenuGroup(models.Model):
	group_id = models.PositiveIntegerField()
	group_name = models.CharField(max_length=50)

	def __str__(self):
		return self.group_name

class MenuItem(models.Model):
	item_id = models.PositiveIntegerField()
	item_name = models.CharField(max_length=100)
	group_id = models.ForeignKey(MenuGroup)

	def __str__(self):
		return self.item_name

class Store(models.Model):
	store_id = models.PositiveIntegerField()
	store_name = models.CharField(max_length=100)

	def __str__(self):
		return self.store_name

class ItemStoreMap(models.Model):
	item_id = models.ForeignKey(MenuItem)
	store_id = models.ForeignKey(Store)


class ItemStoreSellDateMap(models.Model):
	ItemStoreMap_id = models.ForeignKey(ItemStoreMap)
	sell_amount = models.FloatField()
	sell_date = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)



