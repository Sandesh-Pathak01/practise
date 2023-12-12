from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required(login_url='login')
def homepage(request):


    post = models.posts.objects.all()
    comments = models.comments.objects.all()

    context ={
        'post' : post,
        'comments': comments,
    }

    return render(request, 'homepage.html', context)


@login_required(login_url='login')
def profilepage(request, id):

    data = models.profile.objects.get(id=id)

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

         new_comment = models.comments.objects.create(
             
             name = request.user,
             comment = commentt

         )

         new_comment.save()

         return redirect('homepage')
     
     return render(request, 'homepage.html')
