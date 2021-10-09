from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment, Match, Previa
from .forms import CommentForm
from datetime import datetime


class PostListView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mtch'] = Previa.objects.all()
        context['pst'] = Post.objects.all()
        return context
    



class PostDetailView(DetailView):
    model = Post


    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect("detail", slug=post.slug)
        return redirect("detail", slug=self.get_object().slug)


    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['pere'] = Post.objects.all()
        context.update({
            'form': CommentForm()
        })
        return context  

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object

    @property
    def comments(self):
        return self.comment_set.all()

def General_(request):
    post = Post.objects.filter(type='general')
    context = {
        'general': post
    }
    return render(request, 'base.html', context)


def Futbol(request):
    post = Post.objects.filter(type='futbol')
    context = {
        'futbol': post
    }
    return render(request, 'futbol.html', context)


def Juveniles(request):
    post = Post.objects.filter(type='juveniles')
    context = {
        'juveniles': post
    }
    return render(request, 'juveniles.html', context)

def Otros_Dep(request):
    post = Post.objects.filter(type='otros_dep')
    context = {
        'otros_dep': post
    }
    return render(request, 'otros_dep.html', context)




    

    


class PostCreateView(CreateView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post


def get_avg(cant_team, cant_total):
    width_barra = '100'
    avg_team = (float(cant_team)/float(cant_total))*100
    width_team = (float(width_barra)/100)*avg_team
    width_team = str("{0:.2f}".format(width_team))
    width_rest = int(float(width_barra) - float(width_team))
    return width_team, width_rest

def Previa_(request):
    width_barra = '100'
    obj = Previa.objects.first()
    field_object = Previa._meta.get_field('local')
    field_value = field_object.value_from_object(obj)
    datos_partido = Match.objects.filter(local=field_value)
    datos_equipos = Previa.objects.all()
    datos_partido_get = Match.objects.get(local=field_value)
    datos_previa_get = Previa.objects.get(local=field_value)

    width_local, width_rest_local = get_avg(datos_partido_get.victorias_local, datos_partido_get.cant_partidos)
    width_visit, width_rest_visit = get_avg(datos_partido_get.victorias_visita, datos_partido_get.cant_partidos)
    width_emp, width_rest_emp = get_avg(datos_partido_get.empates, datos_partido_get.cant_partidos)







    contextxd = {
        'datos_partido': datos_partido,
        'datos_equipos' : datos_equipos,
        'width_barra'   : width_barra,
        'width_local'   : width_local,
        'width_rest_local' : width_rest_local,
        'width_visit'   : width_visit,
        'width_rest_visit' : width_rest_visit,
        'width_emp'     : width_emp,
        'width_rest_emp': width_rest_emp, 
        'datos_partido_get':datos_partido_get,
        'obj':obj
    }
    return render(request, 'previa.html', contextxd)




