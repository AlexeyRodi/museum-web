from django.contrib import admin
from .models import Exhibit, Exhibition, ExhibitionCategory, MuseumRoom, Museum, Users

admin.site.register(Exhibit)
admin.site.register(Exhibition)
admin.site.register(ExhibitionCategory)
admin.site.register(MuseumRoom)
admin.site.register(Museum)
admin.site.register(Users)