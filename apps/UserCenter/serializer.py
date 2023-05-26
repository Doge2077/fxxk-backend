from rest_framework.serializers import ModelSerializer
from UserCenter import models


class Worker_Serializer(ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"
