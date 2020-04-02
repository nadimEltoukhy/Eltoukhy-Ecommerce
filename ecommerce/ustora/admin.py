from django.contrib import admin
from .models import categories , products ,cart , reviews , checkout
admin.site.register(categories)
admin.site.register(products)
admin.site.register(cart)
admin.site.register(reviews)
admin.site.register(checkout)

# Register your models here.
