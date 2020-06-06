from django.shortcuts import render,redirect   
from .models import Family, Member, Image
from .utils import upload_and_save
import random

def home(request):
    if (request.method == 'POST'):
        file_to_upload = request.FILES.get('img')
        upload_and_save(request, file_to_upload)
        
        return redirect('home')
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts })
# Create your views here.

def mission(request):
    your_missions = []
    mission_easy_list = ['easy_mission1', 'easy_mission2','em3', 'em4', 'em5', 'em6']
    mission_normal_list = ['normal_mission1', 'normal_mission2', 'normal_mission3']
    mission_hard_list = ['hard_mission1', 'hard_mission2', 'hard_mission3']
    your_mission_easy = random.choice(mission_easy_list)
    your_mission_normal = random.choice(mission_normal_list)
    your_mission_hard = random.choice(mission_hard_list)
    your_missions = [your_mission_easy, your_mission_normal, your_mission_hard]
    return render(request, 'misssion.html', {'your_missions': your_missions})

def mission_success(request):
    