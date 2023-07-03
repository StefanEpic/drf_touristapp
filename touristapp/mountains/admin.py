from django.contrib import admin
from .models import User, Level, Coord, Mountain, MountainImage

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Coord)
admin.site.register(Mountain)
admin.site.register(MountainImage)
