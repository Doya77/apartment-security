from django.contrib import admin
from .models import User, Apartment, Visitor, Visit

# Register your models here.
admin.site.register(User)
admin.site.register(Apartment)
admin.site.register(Visitor)
admin.site.register(Visit)