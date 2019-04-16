from django.shortcuts import render


# Create your views here.
class Home():
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)