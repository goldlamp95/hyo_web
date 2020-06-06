from django.shortcuts import render,redirect   
from .models import Family, Member, Image, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
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
    member_images = Image.objects.filter(pk= member_pk)
    return render(request,'indiv_home.html', {'member_images':member_images})

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            individual_id = request.POST["username"],
            individual_password = request.POST["password"]
        )


        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render (request, 'registration/login.html', {'error': error})
        
        auth.login (request, found_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect('home')

        return redirect(request.GET.get('next', '/'))
    
    return render(request, 'registration/login.html')


def signup(request):
    if(request.method == 'POST'):
        #2) 같은 username으로 회원가입을 시도하면 오류가난다
        found_user = User.objects.filter(username=request.POST['individual_id'])

        if(len(found_user)>0):
            error = 'username이 이미 존재합니다' 
            return render(request, 'registration/signup.html', {'error' : error})
        #3) 그런데 error가 떴다는 것을 signup.html에서 메시지가 뜨도록 하게 해야한다

        #1) 새로운 회원가입을 할때 이름을 받아들임
        new_user = User.objects.create_user(
            username = request.POST['individual_id'],
            password = request.POST['individual_password']
        )

        new_member = Member.objects.create (
            name = request.POST['name'],
            birthday = request.POST['birthday'],
            # profile = s3_url + str(request.user.pk)+'/' + now+file_to_upload.name

        )

    

        #4)회원가입과 동시에 로그인 시키키기
        auth.login(request, new_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect ('home')
    return render(request, 'registration/signup.html') #registration 파일안에 있는 signup.html을 빼온다


def family_signup(request):
    if request.method == "POST":
        found_family = Family.objects.filter(family_name = request.POST['family_name'])
        found_user = User.objects.filter(username=request.POST['individual_id'])

        file_to_upload = request.FILES.get('profile_pic')
        print('111🧓🏼',file_to_upload)
        session = Session(
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            region_name = AWS_S3_REGION_NAME
        )

        s3 = session.resource('s3')

        now = datetime.now().strftime("%Y%H%M%S")
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = str(request.user.pk)+'/' + now +file_to_upload.name,
            Body = file_to_upload
        )

        s3_url = 'https://hyohyobucket.s3.ap-northeast-2.amazonaws.com/'

        if (len(found_family)>0) : 
            error = '해당 가족 이름은 이미 존재합니다'
            return render(request, 'registration/family_signup.html', {'error': error})

        print(request.POST)
        if(len(found_user)>0):
            error = 'username이 이미 존재합니다' 
            return render(request, 'registration/signup.html', {'error' : error})


        new_family = Family.objects.create(
            family_name = request.POST['family_name'],
            family_password = request.POST['family_password']
        )

        new_user = User.objects.create_user(
            username = request.POST['individual_id'],
            password = request.POST['individual_password']      
    
        )
        
        new_member = Member.objects.create (
            name = request.POST.get('name', False),
            individual_id= User.objects.get(username = new_user.username),
            individual_password= User.objects.get(password=new_user.password),
            family_password = Family.objects.get(family_password = new_family.family_password),
            birthday = request.POST['birthday'],
            profile = s3_url + str(request.user.pk)+'/' + now+file_to_upload.name
        )
        auth.login(request, new_user, backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect ('home')
    return render(request, 'registration/family_signup.html') #registration 파일안에 있는 signup.html을 빼온다

def logout(request):
    auth.logout(request)
    return redirect('home')

