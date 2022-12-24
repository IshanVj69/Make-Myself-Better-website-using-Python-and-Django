from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def pagination(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except  PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'page.html', {'page': page,
                                         'posts': posts})


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        posts =[]
    else:
      postsTitle = Post.objects.filter(title__icontains=query)
      postsTag = Post.objects.filter(tag__icontains=query)
      posts = postsTitle.union(postsTag)

    params = {'posts': posts, 'query': query}
    return render(request, 'search.html', params)


