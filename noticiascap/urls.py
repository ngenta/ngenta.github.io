from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts import views


from posts.views import (
    Futbol,
    General_,
    Otros_Dep,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    Previa_,
    Juveniles
       
    )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name='list'),
    path('', PostDetailView.as_view(), name='cont'),
    path('<slug>/', PostDetailView.as_view(),name='detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('posts/previa/', Previa_, name='previa'),
    path('posts/juveniles/', Juveniles, name='juveniles'),
    path('', General_, name='general'),
    path('posts/otros_dep/', Otros_Dep, name='otros_dep'),
    path('posts/futbol/', Futbol, name='futbol'),



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)