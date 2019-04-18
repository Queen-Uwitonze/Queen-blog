from django.shortcuts import render,redirect
from .models import Post,Profile,Comments
from .forms import CommentForm,LikeForm

# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  profile = Profile.objects.get()
  comments = Comments.objects.all()
  return render(request, 'index.html',{'posts': posts,'profile':profile,'comments':comments})

def view_blog(request,post_id):
    try:
        posts = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single.html",{"posts": posts})

def view_profile(request):
    profile = Profile.objects.get()
    return render(request, 'profile.html',{'profile':profile})

def popular_news(request,post_id):
    posts = Post.objects.get(id=post_id)
    return redirect("single.html")
    return render(request, 'popular.html',{'posts':posts})

def comment_to_post(request):
   posts = Post.objects.all()
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.user = request.user
          comment.save()
          return redirect('home')
   else:
       form = CommentForm()
   return render(request, 'comments.html', {'form':form})

def com(request,blog_id):
    posts = Post.objects.get(id = blog_id)
    comment = Comments.objects.filter(blog = blog.id).all() 
    likes = Like.objects.filter(blog = blog.id).all() 

    return render(request,'comments.html',{"posts":posts,"comment":comment,"likes":likes}) 

def like(request):
    current_user = request.user
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()

            return redirect('home')

    else:
        form = LikeForm()
    return render(request, 'like.html', {"form": form})