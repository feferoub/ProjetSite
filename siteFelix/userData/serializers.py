# Le serializer convertit les données de l'api en
# JSON et filtre les colonnes à renvoyer

from rest_framework import serializers
from userData.models import UserData

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ('username','password')
		# fields = '__all__'