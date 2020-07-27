from django.db import models


class Technology(models.Model):
    title = models.CharField(max_length=50)
    # percent = models.IntegerField(blank=True)
    # icon = models.CharField(max_length=50, blank=True)
    rank = models.IntegerField(blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    title = models.CharField(max_length=50)
    rank = models.IntegerField(blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='portfolio')
    github_link = models.URLField(blank=True)
    website_link = models.URLField(blank=True)
    date_added = models.DateField()
    ongoing = models.BooleanField(default=True)
    show = models.BooleanField(default=True)
    show_to_home = models.BooleanField(default=True)
    from_scratch = models.BooleanField(default=True)
    tags = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return self.title
