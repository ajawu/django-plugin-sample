from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    is_completed = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)
