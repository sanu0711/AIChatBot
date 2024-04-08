from django.db import models
# Create your models here.
class ChatInteraction(models.Model):
    question=models.CharField(max_length=100)
    response=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question
    
