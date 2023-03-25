from django.contrib import admin
from .models import Cattle,CattleSex,AnimalType,ToolPurpose,Machinery,Goat,GoatSex,SheepSex, Sheep

# Register your models here.

admin.site.register(Cattle)
admin.site.register(CattleSex)
admin.site.register(ToolPurpose)
admin.site.register(AnimalType)
admin.site.register(Machinery)
admin.site.register(Goat)
admin.site.register(GoatSex)
admin.site.register(Sheep)
admin.site.register(SheepSex)
