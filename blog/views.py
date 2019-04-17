from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect("home")

    else:
        form = NewProfileForm()
    return redirect("home")
    return render(request, 'post.html',{'posts':posts})