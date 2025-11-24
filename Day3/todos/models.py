from django.db import models

# Create your models here.

class Todo(models.Model):    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(blank=False)
    created_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title