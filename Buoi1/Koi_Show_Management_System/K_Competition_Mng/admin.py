from django.contrib import admin
from .models import competition, register
# Register your models here.
# admin.site.register(competition)

class competitionAdmin(admin.ModelAdmin):
  list_display = ("name", "start_date", "end_date",)

class registerAdmin(admin.ModelAdmin):
  list_display = ("name", "start_date", "gender", "age", "size",)
  
admin.site.register(competition, competitionAdmin)
admin.site.register(register, registerAdmin)