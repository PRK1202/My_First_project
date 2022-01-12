from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(user)
admin.site.register(HR)
admin.site.register(Manager)
admin.site.register(Developer)
admin.site.register(Tester)