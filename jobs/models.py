from django.db import models

# models.Model allows us to create a Job class along with some background django code we need

class Job(models.Model):
    # upload_to="" -> inside the media folder, we can create additional folders to upload our images to.
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=250)
