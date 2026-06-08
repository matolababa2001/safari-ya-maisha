from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import translation
from django.utils.translation import gettext as _
from django.db.models import Q



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):

    return render(
        request,
        'profile.html'
    )

def home(request):
    lang = request.session.get('lang', 'sw')

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'posts': posts,
        'lang': lang
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')

        Comment.objects.create(
            post=post,
            name=name,
            comment=comment
        )

        return redirect('post_detail', id=id)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments
    })

def neno_la_mungu(request):
    lang = get_lang ( request )
    posts = Post.objects.filter(category='neno')
    return render(request, 'category.html', {
        'title': 'Neno la Mungu',
        'posts': posts
    })

def tiba_lishe(request):
    lang = get_lang ( request )
    posts = Post.objects.filter(category='lishe')
    return render(request, 'category.html', {
        'title': 'Tiba Lishe',
        'posts': posts
    })

def siri_za_ndoa(request):
    lang = get_lang ( request )
    posts = Post.objects.filter(category='ndoa')
    return render(request, 'category.html', {
        'title': 'Mahusiano ya Ndoa',
        'posts': posts
    })
def change_language(request, lang):
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return redirect(request.META.get('HTTP_REFERER'))
def set_language(request, lang):
    request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))
def get_lang(request):
    return request.session.get('lang', 'sw')  # default Swahili
def home(request):
    lang = get_lang(request)

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'posts': posts,
        'lang': lang
    })
def search(request):
    query = request.GET.get('q')

    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )

    return render(request, 'search.html', {
        'posts': posts,
        'query': query
    })
@login_required
def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', post_id=post.id)