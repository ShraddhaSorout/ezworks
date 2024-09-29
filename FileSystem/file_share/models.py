from django.db import models
from django.contrib.auth.models import User

class SharedFile(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} shared by {self.uploader} with {self.recipient}"
