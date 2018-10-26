from django.contrib import admin
from . import models


admin.site.register(models.customers)
admin.site.register(models.logins)
admin.site.register(models.categories)
admin.site.register(models.delivery_addresses)
admin.site.register(models.orders)
admin.site.register(models.Products)
admin.site.register(models.order_items)
admin.site.register(models.admins)

