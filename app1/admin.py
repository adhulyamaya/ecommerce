from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(custom_user)
admin.site.register(Product)
admin.site.register(category)
