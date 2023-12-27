from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required(login_url='login')
def homepage(request):


    post = models.posts.objects.all()


    context ={
        'post' : post,
    }

    return render(request, 'homepage.html', context)


@login_required(login_url='login')
def profilepage(request, id):

    data = models.profile.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('fullName')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        gender = request.POST.get('gender')

        edited_data = models.profile.objects.get(id=id)

        edited_data.name = name
        edited_data.address = address
        edited_data.bio = bio
        edited_data.gender = gender

        edited_data.save()

        return redirect('profileedit')


    context = {
        'data': data,
    }

    return render(request, 'profilepage.html', context)


@login_required(login_url='login')
def profile(request):

    data = models.profile.objects.get(username = request.user)

    context = {
        'data' : data,
    }


    return render(request, 'Firstprofile.html', context)


def add_posts(request):

    if request.method == 'POST':

        description = request.POST.get('description')
        postpic = request.FILES.get('postpic')
        user = models.profile.objects.get(username = request.user)
        

        new_post = models.posts.objects.create(

            name = request.user,
            description = description,
            profile_pic = user,

        )

        new_post.post_img = postpic

        new_post.save()

        return redirect('homepage')


    return render(request, 'homepage.html')


def add_comments(request):
     
     if request.method == 'POST':
         
         commentt = request.POST.get('comment')
         post_id = request.POST.get('post_id')

         post_instance = models.posts.objects.get(id=post_id)

         new_comment = models.comments.objects.create(
             
             post_comment = post_instance,
             name = request.user,
             comment = commentt,

         )

         new_comment.save()

         return redirect('homepage')
     
     return render(request, 'homepage.html')


def likes(request):
    
    if request.method == 'POST':
        user = request.user
        post_id = request.POST.get('post_id')

        post_instance = models.posts.objects.get(id=post_id)

        if post_instance.likes.filter(id=user.id).exists():
            post_instance.likes.remove(user)
        else:
            post_instance.likes.add(user)

        return redirect('homepage')

