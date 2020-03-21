from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post,Ingredient
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def recipe_list(request):

    post = Post.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')
    
    number_post = Post.objects.all().count()
    
    search_term = ""
    if 'search' in request.GET:
        search_term = request.GET['search']
        post = post.filter(description__icontains=search_term)
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post_pgn = paginator.get_page(page)
    return render(request, 'recipe_list.html', {'post_pgn': post_pgn, 'number_post': number_post, 'search_term': search_term})


def select_ingredients(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post = form.save()

    return render(request, 'recipe_detail.html', {'post': post, 'form': form})



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
            form.save()
            post.save()

            return redirect('recipe_detail', pk=post.pk)

        else:
            form = PostForm(instance=post)

    return render(request, 'recipe_edit.html', {'form': form})
