from django.contrib import admin
# Register your models here.
from .models import Bb
from .models import Rubric

class BbAbmin(admin.ModelAdmin):
    list_display = ('title', 'content','price','published','rubric','img','image_img')
    list_display_links = ('title','content','img','image_img')
    search_fields = ('title','content',)
    readonly_fields = ['image_img', ]

admin.site.register(Bb,BbAbmin)
admin.site.register(Rubric)
