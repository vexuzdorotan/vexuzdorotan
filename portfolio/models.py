from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='portfolio')
    github_link = models.URLField(blank=True)
    website_link = models.URLField(blank=True)
    date_added = models.DateField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
