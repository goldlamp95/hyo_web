from django.shortcuts import render,redirect   
from .models import Family, Member, Image, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .utils import upload_and_save
def new(request):
    if (request.method == 'POST'):      
        file_to_upload = request.FILES.get('img')
        upload_and_save(request, file_to_upload)   
    return redirect('home')


def home(request):
    images = Image.objects.all()
    members = Member.objects.all()
    return render(request, 'home.html', {'images':images, 'members': members})

def detail(request, image_pk):
    chosen_image= Image.objects.get(pk = image_pk)
    if request.method =="POST":
        Comment.objects.create(
            post = chosen_image,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', image_pk)
    return render(request, 'detail.html', {'chosen_image': chosen_image})

def delete_comment(request, image_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail', image_pk)

def edit_comment(request, image_pk, comment_pk):
    comment = Comment.objects.get(pk= comment_pk)
    if request.method == 'POST':
        Comment.objects.filter(pk = comment_pk).update(
            content= request.POST['content']
        )
        return redirect ('detail', image_pk)
    return render(request, 'edit_comment.html')

def indiv_home(request, member_pk):
    member_images = Image.object.filter(pk= member_pk)
    return render(request,'indiv_home.html', {'member_images':member_images})

def todo(request):
    tasks = Todolist.objects.all().order_by('due')
    context = {'tasks': tasks}
    return render(request,'todo.html', context)

def todo_new(request):
    if request.method == 'POST':
        Todolist.objects.create(
            task = request.POST['task'],
            due = request.POST['due'],
            tag = request.POST['tag'],
            list_author = request.user
        )
        return redirect ('todo')
    return render(request,'todo_new.html')

def todo_delete(request, task_pk):
    task = Todolist.objects.get(pk=task_pk)
    task.delete()
    return redirect ('todo')

