from django.db import models



class Cipher(models.Model):
    text = models.TextField()
    key = models.IntegerField(blank=True, default=1)
    vig_key = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return self.text
