from django.db import models


class blog2(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='sad/')
    def easy(self):
        return self.body[:200]
    def timesui(self):
        self.pub_date.strftime("%m %d %Y")
    def __str__(self):
        return self.title
# 1) create a blog model
# 2) add the blog app to the setting
# 3) create a migration
# 4) make migrations
# 5) add to the admin
