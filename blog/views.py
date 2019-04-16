from django.shortcuts import render


# Create your views here.
def index(request):
  message = "welcome"
  return render(request, 'index.html')