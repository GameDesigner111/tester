from django.db import models


class Question(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_true = models.BooleanField(default=False)
