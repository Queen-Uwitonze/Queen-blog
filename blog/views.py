from django.shortcuts import render,redirect
from .models import Post,Profile,Comments
from .forms import CommentForm

# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  profile = Profile.objects.get()
  comments = Comments.objects.all()
  return render(request, 'index.html',{'posts': posts,'profile':profile,'comments':comments})
    
def comment_to_post(request):
   posts = Post.objects.all()
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.user = request.user
          comment = Comments.objects.filter(comment =id).all() 
        #   comment.save()
          return redirect('home')
   else:
       form = CommentForm()
   return render(request, 'comments.html', {'form':form})

def com(request,blog_id):
    posts = Post.objects.get(id = blog_id)
    comment = Comments.objects.filter(blog = blog.id).all() 
    likes = Like.objects.filter(blog = blog.id).all() 

    return render(request,'comments.html',{"posts":posts,"comment":comment,"likes":likes}) 

