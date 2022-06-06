from django.db import models


class Emoji(models.Model):
    text = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return f'{self.text}: {self.score}'
