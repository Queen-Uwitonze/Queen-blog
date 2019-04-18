from django.shortcuts import render,redirect
from .models import Post,Profile,Comments
from .forms import CommentForm,LikeForm
from .forms import SubscriptionForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib import messages
from django.core.signing import BadSignature
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _, ugettext_lazy


# Create your views here.
def index(request):
  message = "welcome"
  posts = Post.objects.all()
  profile = Profile.objects.get()
  
  return render(request, 'index.html',{'posts': posts,'profile':profile})

def view_blog(request,post_id):
    try:
        posts = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single.html",{"posts": posts})

def view_profile(request):
    profile = Profile.objects.get()
    # form = NewsLetterForm(request.POST)
    # if request.method == 'POST':
       
    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']
    #         email = form.cleaned_data['email']
    #         recipient = NewsLetterRecipients(name = name,email =email)
    #         recipient.save()
    #         HttpResponseRedirect('profile')

    #     else:
    #         form = NewsLetterForm()
    return render(request, 'profile.html',{'profile':profile})

def comment_to_post(request,post_id):
   posts = Post.objects.get(id=post_id)
   comments=Comments.objects.filter(post=posts)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.user = request.user
          comment.post=posts
          comment.save()
          return redirect('comments',posts.id)
   else:
       form = CommentForm()
   return render(request, 'comments.html', {'form':form,'posts':posts,'comments':comments})


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


def multiple_forms(request):
    if request.method == 'POST':
        posts = Post(request.POST)
        subscription_form = SubscriptionForm(request.POST)
        if contact_form.is_valid() or subscription_form.is_valid():
            # Do the needful
            return HttpResponseRedirect(reverse('form-redirect') )
    else:
        contact_form = Post()
        subscription_form = SubscriptionForm()

    return render(request, 'subscription.html', {
        'contact_form': contact_form,
        'subscription_form': subscription_form,
    })