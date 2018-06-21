from django.contrib import admin
from post.models import Tag
from post.models import Post

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)