from rest_framework.serializers import (
    ModelSerializer,
    models,
)
from .models import receive_msg

class msgSeriarizer(ModelSerializer):

    class Meta:
        model = receive_msg
        fields = '__all__'
    def create(self,validated_data):
        return receive_msg.objects.create(**validated_data)