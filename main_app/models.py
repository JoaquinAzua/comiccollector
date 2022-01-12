from django.db import models

# Create your models here.

class Comic(models.Model):
    title = models.CharField(max_length=50)
    issue = models.IntegerField()
    year = models.IntegerField()
    publisher = models.CharField(max_length=20)


    def __str__(self):
        return f"({self.id}) - {self.title}"


# comics = [
#     Comic('X-Men', 1, 1991, 'Marvel'),
#     Comic('Star Wars', 1, 2015, 'Marvel'),
#     Comic('Batman Detective', 1000, 2019, 'DC'),
#     Comic('Darth Vader', 1, 2017, 'Marvel')
# ]