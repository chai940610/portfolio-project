from django.db import models

# 1) create a blog model
class blog2(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='sad/')
# 2) add the blog app to the setting
# 3) create a migration
# 4) make migrations
# 5) add to the admin
