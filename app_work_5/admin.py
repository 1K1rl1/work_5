from django.contrib import admin

# Register your models here.
from .models import Advertisement_2

class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'datefilt', 'auction', 'dateupfilt', 'image_tag']
    list_filter = ['auction', 'created_at']
    actions = ['makeauction_off', 'makeauction_on']
    fieldsets = (
        ('Маркетинг', {
            'fields': ('title', 'description', 'image')
        }),
        
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes':['collapse']
        }),
        
        )
    @admin.action(description = 'Убрать торг')
    def makeauction_off(self, request, queryset):
        queryset.update(auction = False)
    @admin.action(description = 'вернуть торг')
    def makeauction_on(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisement_2, AdvAdmin)