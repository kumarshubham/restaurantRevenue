from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MenuGroup)
admin.site.register(MenuItem)
admin.site.register(Store)
admin.site.register(ItemStoreMap)
admin.site.register(ItemStoreSellDateMap)
