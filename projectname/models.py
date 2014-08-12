from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy

# Create your models here.
class Projectname(models.Model):
    street = models.CharField(max_length = 400)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.IntegerField()
    Fields = '__all__'

    def get_absolute_url(self):
        return reverse('projectname-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str.format('{0}, {1}, {2} - {3}', self.street, self.city, self.state, self.zipcode)
