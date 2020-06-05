from django.shortcuts import render,redirect   
from .models import Post
from .utils import upload_and_save

def home(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get('img')
        upload_and_save(request, file_to_upload)
        
        return redirect('home')
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts })
# Create your views here.
