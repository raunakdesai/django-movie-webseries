from django.contrib import admin
from projx.models import Movies,Actor,Genre,Series,Season,Episode

# Register your models here.
admin.site.register(Movies)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)