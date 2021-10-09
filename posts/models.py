from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from ckeditor.fields import RichTextField



class User(AbstractUser):
    pass
    def __str__(self):
        return self.username


class Post (models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    type = models.CharField(max_length=20, choices=(('general', 'general'),('juveniles', 'juveniles')), default='general')

    def __str__(self):
        return self.title
        return render(request, "post_detail.html", locals())

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

        

class Previa(models.Model):
    competicion= models.ImageField()
    fecha = models.CharField(max_length=5)
    local = models.CharField(max_length=100)
    visit = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    imglocal = models.ImageField()
    imgvisit = models.ImageField()
    


class Match(models.Model):
    local = models.CharField(max_length=100)
    visit = models.CharField(max_length=100)
    cant_partidos = models.CharField(max_length=10)
    victorias_local = models.CharField(max_length=10)
    victorias_visita = models.CharField(max_length=10)
    empates = models.CharField(max_length=10)
    goles_local = models.CharField(max_length=10)
    goles_visita = models.CharField(max_length=10)



class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.TextField()


    def __str__(self):
        return self.user.name



class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.user.username
    