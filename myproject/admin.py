from re import T
from django.contrib import admin
from  .models import Project,Review,Tag

# Register your models here.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

# # @admin.register(Project)
# # class ProjectAdmin(admin.ModelAdmin):
# #     list_display = ['name','img','language','description','created_at']