from django.contrib import admin
from myapp.models import Article
from myapp.models import User

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date_time','category')

admin.site.register(Article,ArticleAdmin)
admin.site.register(User)
