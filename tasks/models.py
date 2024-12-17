from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(TimestampedModel):

    class State(models.TextChoices):
        COMPLETED = "COMPLETED"
        IN_PROGRESS = "IN_PROGRESS"
        PENDING = "PENDING"

    due_date = models.DateField()
    state = models.CharField(max_length=15, choices=State.choices, default=State.PENDING)
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=200)


    def __str__(self):
        return self.title
