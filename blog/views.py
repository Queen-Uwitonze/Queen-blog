from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  return render(request, 'index.html',{'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return redirect('home')
    return render(request,'post.html',{'posts': posts})
    
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, blog=post,
                                   title='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'detail.html',{'posts': posts})

    

