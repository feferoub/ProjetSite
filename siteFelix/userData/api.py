from userData.models import UserData
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserDataSerializer
from django_filters import rest_framework as filters

class UserDataViewSet(viewsets.ModelViewSet):
	queryset = UserData.objects.all()
	permission_classes = [
	permissions.AllowAny
	]
	serializer_class = UserDataSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ['username',]

	# @action(methods=['get'], detail=False)
	# def getUserInfo(self,request):
	# 	usernames = self.get_queryset().get(username='Feli')
	# 	serializer = self.get_serializer_class()(usernames)
	# 	return Response(serializer.data)