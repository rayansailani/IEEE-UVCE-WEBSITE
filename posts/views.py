from django.shortcuts import render, get_object_or_404, redirect
from .models import PostImage, Post
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.

# function to check if user is an SIG head


def is_sh(request):
    user = request.user
    sig_heads = Account.objects.all().filter(is_sig_head=True)
    return user in sig_heads

# function to display the gallery of all events


def post_view(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'posts/post.html', context)

# function to display the indivisual events


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post': post,
        'photos': photos,
    }
    return render(request, 'posts/detail.html', context)

# function to create a new gallery of events


@login_required(login_url="/accounts/login/")
def create_post_view(request):
    if request.user.is_sig_head:
        if request.method == 'POST':
            length = request.POST.get('length')
            title = request.POST.get('title')
            # poster = request.POST.get('poster')
            poster = request.FILES.get('poster')

            post = Post.objects.create(
                title=title,
                Poster=poster,
            )

            for file_num in range(0, int(length)):
                PostImage.objects.create(
                    post=post,
                    image=request.FILES.get(f'images{file_num}')
                )
            return redirect('post')
        else:
            return render(request, 'posts/post-create.html')
    else:
        return render('home_page')
