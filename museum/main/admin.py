from django.contrib import admin
from .models import Exhibit, Exhibition, Exhibition_Category, Museum_Room, Museum, Users

admin.site.register(Exhibit)
admin.site.register(Exhibition)
admin.site.register(Exhibition_Category)
admin.site.register(Museum_Room)
admin.site.register(Museum)
admin.site.register(Users)