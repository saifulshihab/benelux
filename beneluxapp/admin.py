from django.contrib import admin

# Register your models here.
from .models import projects, over_para, diensten_para

admin.site.register(projects)
admin.site.register(over_para)
admin.site.register(diensten_para)