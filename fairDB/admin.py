from django.contrib import admin
from .models import Product, Manufacturer, Score, Certification, UserReview, Ingredient

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Score)
admin.site.register(Certification)
admin.site.register(UserReview)
admin.site.register(Ingredient)