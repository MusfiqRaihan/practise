from django.db import models


class MyTest(models.Model):
    image = models.ImageField(upload_to='test_image/')
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(max_length=500, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    comment = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
