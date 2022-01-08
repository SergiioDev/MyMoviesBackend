from django.contrib import admin

# Register your models here.
from PlayLists.models import WatchList,WatchLists

admin.site.register(WatchList)
admin.site.register(WatchLists)
