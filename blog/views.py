from django.shortcuts import render,get_object_or_404
from .models import Post,Profile,Comments
from .forms import CommentForm

# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  profile = Profile.objects.get()
  return render(request, 'index.html',{'posts': posts,'profile':profile})
    
def comment_to_post(request):
   posts = Post.objects.all()
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comments = form.save(commit=False)
          comments.user = request.user
          comments = Comments.objects.all()
          comments.save()
          return redirect('post_detail')
   else:
       form = CommentForm()
   return render(request, 'comments.html', {'form':form,'comments':comments})

    

