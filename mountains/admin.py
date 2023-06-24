from django.contrib import admin
from .models import Users, Level, Coords, Mountain, MountainImages

admin.site.register(Users)
admin.site.register(Level)
admin.site.register(Coords)
admin.site.register(Mountain)
admin.site.register(MountainImages)
