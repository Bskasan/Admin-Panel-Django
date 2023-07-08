from django.contrib import admin
from .models import *

admin.site.site_title = 'RoninDev'
admin.site.site_header = 'Admin Panel - RoninDev'
admin.site.index_title = 'RoninDev - Index Page'


# Register your models here.
admin.site.register(Product)