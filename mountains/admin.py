from django.contrib import admin
from .models import Author, Level, Coords, Mountain, MountainImages

admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Coords)
admin.site.register(Mountain)
admin.site.register(MountainImages)
