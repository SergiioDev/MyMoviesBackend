from rest_framework import serializers

from PlayLists.models import WatchLists


class WatchListSerializers(serializers.ModelSerializer):
    model = WatchLists
    fields = '__all__'
    depth = 1
