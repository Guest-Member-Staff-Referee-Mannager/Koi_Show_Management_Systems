from django.contrib import admin
from .models import competition
# Register your models here.
# admin.site.register(competition)

class competitionAdmin(admin.ModelAdmin):
  list_display = ("name", "start_date", "end_date",)
  
admin.site.register(competition, competitionAdmin)