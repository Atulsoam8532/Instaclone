from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Post,Room,Messeges,Comment
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import date
import time
# Create your views here.

def home(request):
    posts = Post.objects.filter(Q(profiles__follower = request.user))
    comment = Comment.objects.filter(user=request.user)
    profile = Profile.objects.get(user = request.user)
    
    return render(request, 'home.html',{'post':posts,'profi':profile})

def logins(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwo = request.POST.get('password')
        user = authenticate(username= uname,password = passwo)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print('invalid user')
    return render(request, 'login.html')


def singup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mnum = request.POST.get('phone')
        dob = request.POST.get('dd')+'-'+ request.POST.get('mm')+'-'+  request.POST.get('yyyy')
        uname = request.POST.get('uname')
        pas = request.POST.get('pword')
        make_user = User.objects.create_user(first_name = fname,last_name=lname,email=email,username=uname,
        password = pas)
        make_user.save()
        profil = Profile.objects.create(user = make_user, Mobile_number= mnum,DOB= dob)
        profil.save()
        return redirect('login')
    return render(request, 'signup.html')


def logouts(request):
    logout(request)
    return redirect('login')

def profiles(request):
    profil = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user = request.user)
    postnum = posts.count()
    return render(request,'profile.html',{'profile':profil,'post':posts,'postnum':postnum})

def search(request):
    searchs = request.GET.get('search')
    profil = Profile.objects.filter(user__username__icontains =searchs)
    details = User.objects.filter(first_name__icontains=searchs)
    profile = Profile.objects.get(user= request.user)
    return render(request,'search.html',{'result':profil,'details':details,'username':searchs,'profi':profile})

def follow(request,id,username):
    profil = Profile.objects.get(id = id)
    following = Profile.objects.get(user= request.user)
    if request.user in profil.follower.all():
        profil.follower.remove(request.user)
        following.following.remove(profil.user)
    else:
        profil.follower.add(request.user)
        following.following.add(profil.user)
    return redirect(f'/search?search={username}')

def follow_profile(request,id,username):
    profil = Profile.objects.get(id = id)
    
    following = Profile.objects.get(user= request.user)
    if request.user in profil.follower.all():
        profil.follower.remove(request.user)
        following.following.remove(profil.user)
    else:
        profil.follower.add(request.user)
        following.following.add(profil.user)
    return redirect(f'/showprofile/{id}/{username}')

def upload_post(request):
    if request.method == 'POST':
        img = request.FILES.get('image')
        pro = Profile.objects.get(user = request.user)
        upload = Post.objects.create(user = request.user,posts = img,profiles=pro)
        if upload:
            upload.save()
            return redirect('home')
    return render(request,'upload.html')

def edit(request):
    prof = Profile.objects.get(user= request.user)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        bio = request.POST.get('about')
        imag = request.FILES.get('image')
        email = request.POST.get('email')
        mnum = request.POST.get('mnum')
        uname = request.POST.get('uname')
        prof.Bio = bio
        prof.profile_pic = imag
        prof.Mobile_number= mnum
        prof.save()
        user = User.objects.get(username = request.user)
        user.first_name = fname
        user.last_name =lname
        user.email = email
        user.username=uname
        user.save()
        return redirect('profile')

    return render(request,'edit.html',{'prof':prof})


def clicked_profile(request,id,user):
    #posts = Post.objects.get(user_id=id)
    clicked = Profile.objects.get(user_id = id)
    users = User.objects.get(username = user)
    post_count = Post.objects.filter(user_id =id)
    postnum = post_count.count()
    profi = Profile.objects.get(user= request.user)
    return render(request,'user_profile.html',{'profi':profi,'postnum':postnum,'u':users,'profile':clicked,'post':post_count})
def follow_custom(request,id,user,username):
    profil = Profile.objects.get(id = user)
    print(profil.user)
    following = Profile.objects.get(user= request.user)
    if request.user in profil.follower.all():
        profil.follower.remove(request.user)
        following.following.remove(profil.user)
    else:
        profil.follower.add(request.user)
        following.following.add(profil.user)
    return redirect(f'/showprofile/{id}/{username}')

def follow_list(request,user):
    users = Profile.objects.get(id=user)
    curent = Profile.objects.filter(following = users.user)
    post_count = Post.objects.filter(user_id =user)
    postnum = post_count.count()
    return render(request,'follower_list.html',{'profil':curent,'postnum':postnum,'profile':users})
def following(request,user):
    users = Profile.objects.get(id=user)
    curent = Profile.objects.filter(follower = users.user)
    post_count = Post.objects.filter(user_id =user)
    postnum = post_count.count()
    return render(request,'following_list.html',{'profil':curent,'postnum':postnum,'profile':users})
   

def like(request,id):
    liked = Post.objects.get(id=id)
    if request.user in liked.likes.all():
        liked.likes.remove(request.user)
    else:
        liked.likes.add(request.user)
    return redirect('home')

def reel_show(request):
    return render(request,'reels.html')
def upload_reel(request):
    pass

def chat(request,id):
    profi =User.objects.get(id=id).username
    room = str(profi)+str(request.user)
    if Room.objects.filter(room_name = room).exists():
        room_name = room
    else:
        room_name = str(request.user)+str(profi)
    roomn = Messeges.objects.filter(room_id = room_name)
    
    if request.method =='POST':
        msg = request.POST.get('msg')
        create = Messeges.objects.create(msg=msg,user=request.user,room_id =room_name)
        create.save()
    profile = Profile.objects.get(user=request.user)
    following = profile.following.all()
    return render(request,'chat.html',{'room':roomn,'chats':following,'profile':profile,'person':profi})

def room(request,id):
    user_1 = request.user
    user_2 = User.objects.get(id= id)
    room = str(user_1)+str(user_2)
    room2 = str(user_2)+str(user_1)
    print(room)
    if Room.objects.filter(room_name = room).exists() or Room.objects.filter(room_name = room2):
        pass
    else:
        room = Room.objects.create(user_1 = user_1,user_2 = user_2,room_name=room,is_created = True)
        room.save()
    return redirect(f'/chat/{id}')

def showchat(request):
    profile = Profile.objects.get(user=request.user)
    following = profile.following.all()
    return render(request,'showchat.html',{'profile':profile,'chats':following})

def add_comment(request,id):
    post = Post.objects.get(id = id)
    print(post.user)
    if request.method == 'POST':
        cmnt = request.POST.get('cmnt')
        comment = Comment.objects.create(comment=cmnt,user = request.user,post = post)
        comment.save()
    return redirect('home')

def grid(request):
    return render(request,'grid.html')


def save_post(request,id):
    post = Post.objects.get(id = id)
    if request.user in post.saved_user.all():
        post.saved_user.remove(request.user)
        
        post.save()
    else:
        post.saved_user.add(request.user)
        post.save()

    return redirect('home')

def show_save_post(request):
    post = Post.objects.all()
    return render(request,'saved_post.html',{'post':post})






   