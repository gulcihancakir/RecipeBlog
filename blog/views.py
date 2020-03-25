from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Post, Ingredient
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.db import models


def recipe_list(request):

    post = Post.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')

    number_post = Post.objects.all().count()

    ings = Ingredient.objects.values('name').annotate(
        Count('post')).order_by('-post__count')[:5]

    search_term = ""
    if 'search' in request.GET:
        search_term = request.GET['search']
        post = post.filter(Q(description__icontains=search_term)
                           | Q(recipe_name__icontains=search_term))

    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post_pgn = paginator.get_page(page)

    return render(request, 'recipe_list.html', {'post_pgn': post_pgn, 'number_post': number_post, 'search_term': search_term, 'ings': ings})



def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    post.likes.add(request.user)

    return HttpResponseRedirect(post.get_absolute_url())


def recipe_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'recipe_detail.html', {'post': post})


def recipe_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('recipe_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'recipe_edit.html', {'form': form})


def recipe_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('recipe_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'recipe_edit.html', {'form': form, 'post': post})
