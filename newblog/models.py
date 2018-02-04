from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt=models.CharField(max_length=200,blank=True)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk': self.pk})

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    def save(self,*args, **kwargs):
        if not self.excerpt:
            self.excerpt=self.body[:10]
        super(Post,self).save(*args, **kwargs)


    class Meta:
        ordering=['-created_time']



