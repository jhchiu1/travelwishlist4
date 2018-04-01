from django.db import models

# Create a data object to store information about the places

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    visited_date = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)


    def __str__(self):
        return '%d: %s visited? %s on %s' % (self.pk, self.name, self.visited, self.visited_date)