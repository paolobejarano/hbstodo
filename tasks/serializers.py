from tasks.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "due_date", "state", "title", "detail"]

    def validate_title(self, value):
        """
        Validate that the title has at least one non-whitespace character.
        """
        if not value.strip():
            raise serializers.ValidationError("Title must contain at least one character.")
        return value
