from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name="home"),
    url(r'^comments/', views.comment_to_post, name='comments'),
    url(r'^com/(\d+)', views.com, name='com'),
    url(r'^likes/', views.like, name='like'), 
    url(r'^profile/', views.view_profile, name='view_profile'), 
    url(r'^popular/(\d+)', views.popular_news, name='popular_news'), 
    url(r'^single/(\d+)', views.view_blog, name='view_blog'), 
    
    
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)