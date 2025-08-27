from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks",
    )

    class Meta:
        ordering = ["is_completed", "-datetime"]

    def __str__(self):
        return (
            f"{self.content}, tags: {', '.join(tag.name for tag in self.tags.all())}"
        )
