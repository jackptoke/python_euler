from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic a user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __init__(self):
        """Return a string representation of the model"""
        # super().__init__(*args, **kwargs)
        return self.text