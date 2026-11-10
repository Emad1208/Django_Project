from django.db import models

class Post(models.Model):
    # author
    # image
    title = models.CharField(max_length = 255)
    content = models.TextField()
    # category
    # tag
    counted_views = models.IntegerField(default= 0)
    status = models.BooleanField(null= True)
    published_date = models.DateField(null= True)
    created_date = models.DateField(auto_now_add= True)
    updated_date = models.DateField(auto_now= True)



