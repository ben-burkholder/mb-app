from django.db import models

class Post(models.Model):
    text = models.TextField()

    def _str_(self):
      return str(self.text)[:50]

