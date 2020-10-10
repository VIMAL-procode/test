from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=180)

    def __str__(self):
        #return self.title
        return '%s %s-' % (self.title, self.body)