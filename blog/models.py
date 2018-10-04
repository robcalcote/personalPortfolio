from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Create a migration

# Migrate

# Add to the admin