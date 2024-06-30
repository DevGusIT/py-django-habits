from django.db import models

class Habit(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
