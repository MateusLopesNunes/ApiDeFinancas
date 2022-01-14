from rest_framework import serializers
from .models import User, Finance
from financas import validator

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'

    def validate(self, data):
        if not validator.nome_valid(data['name']):
            raise serializers.ValidationError({'name': 'O campo nome deve ter de 5 a 149 caracteres '})
        return data

class FinanceSerializer(serializers.ModelSerializer):
    class Meta():
        model = Finance
        fields = '__all__'

class ListFinanceToUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    class Meta():
        model = Finance
        fields = '__all__'