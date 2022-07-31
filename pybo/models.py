from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self) :
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


# Field types used in Django :
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

# Django document :
# https://docs.djangoproject.com/en/4.0/topics/db/queries/