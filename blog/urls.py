from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name="home"),
    url(r'^comments/', views.comment_to_post, name='comments'),
    url(r'^com/(\d+)', views.com, name='com'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)