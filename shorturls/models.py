from django.db.models import *


# Create your models here.
class URL(Model):
    path = URLField(max_length=254)
    key = CharField(max_length=10, unique=True)
    date = DateTimeField(auto_now_add=True)
    hit = IntegerField(default=0)

    def __str__(self):
        return self.key

    def increment(self):
        self.hit += 1
        self.save()
