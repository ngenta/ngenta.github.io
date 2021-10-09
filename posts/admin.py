from django.contrib import admin

from .models import Post, PostView, Comment, Like, User, Match, Previa

admin.site.register(Post)
admin.site.register(Match)
admin.site.register(Previa)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User)