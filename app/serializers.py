from app.models import *

from rest_framework import serializers
class NameSerializer(serializers.Serializer):
    email=serializers.EmailField()
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)
    image=serializers.ImageField()



class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MyModel
        fields= ('creator','image_url')