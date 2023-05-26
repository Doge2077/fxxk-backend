from rest_framework.serializers import ModelSerializer
from UserCenter import models


class User_ser(ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"
