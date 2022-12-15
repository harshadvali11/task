from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app import serializers
from app.models import *
from .serializers import ImageUploadSerializer


class SampleViewset(viewsets.ViewSet):
    serializer_class=serializers.NameSerializer
    def list(self,request):
        data=UserProfile.objects.values()
        return Response({'data':data})
    def create(self,request):
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            email=data._validated_data.get('email')
            
            first_name=data._validated_data.get('first_name')
            last_name=data.validated_data.get("last_name")
            password=data.validated_data.get('password')
            image=data.validated_data.get('image')
            u=UserProfile.objects.get_or_create(email=email,first_name=first_name,last_name=last_name)[0]
            u.set_password(password)
            u.is_staff=True
            u.is_superuser=True
            u.save()
            m=MyModel.objects.get_or_create(creator=u,image_url=image)[0]
            m.save()
            return Response({'message':"user is created successfully"})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        return Response({'data':UserProfile.objects.filter(id=pk).values()})
    


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = ImageUploadSerializer

