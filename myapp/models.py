from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(u'博客标题',max_length=100)
    category=models.CharField(u'博客标签',max_length=50,blank=True)
    date_time=models.DateTimeField(u'发布日期',auto_now_add=True)
    content=models.TextField(u'博客正文',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date_time']
