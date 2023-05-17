from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','owner','rasm1']
admin.site.register(Portfolio,AdminPortfolio)

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,AdminCategory)

class AdminService(admin.ModelAdmin):
    list_display = ['id','name','rasm1']
admin.site.register(Services,AdminService)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','name','job','desc','rasmi']
admin.site.register(Team,AdminTeam)

class Admincall(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']
admin.site.register(Adminga_murojaat,Admincall)

