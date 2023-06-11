from rest_framework.serializers import ModelSerializer
from UserCenter import models


class User_Serializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class Worker_Serializer(ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"


class Job_Serializer(ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"
