from django.contrib import admin
from .models import Category, Location, Pictures

# Register your models here.
class PicturesAdmin(admin.ModelAdmin):
    filter_horizontal =('image_category',)

class CategoryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Pictures,PicturesAdmin)

