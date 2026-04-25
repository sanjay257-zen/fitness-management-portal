from django.contrib import admin

# Import your models here
# from .models import YourModel

class PlannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'activity')
    search_fields = ('name',)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'availability')
    search_fields = ('name',)

class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'client', 'progress', 'session_count')

class PredictionsAdmin(admin.ModelAdmin):
    list_display = ('client', 'predicted_progress', 'date')

# Register your models here
# admin.site.register(YourModel, YourModelAdmin)

admin.site.register(PlannerAdmin)
admin.site.register(TrainerAdmin)
admin.site.register(StatisticsAdmin)
admin.site.register(PredictionsAdmin)