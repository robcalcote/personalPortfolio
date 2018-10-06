from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # This function will return the title as the name of the blog post on the admin page
    # rather than an arbitrary primary key that was previously shown
    def __str__(self):
        return self.title

    # This function will return only the first 100 characters of a blog post to avoid showing too much
    def summary(self):
        return self.body[:100]

    # This function will parse out a DateTimeField into only showing the Date in MMM DD, YYYY format
    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e, %Y')