# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Post

# Devuelve el listado de posts
def index(request):
    posts = get_list_or_404(Post.objects.order_by('date'))
    context = { 'lista_posts': posts }
    return render(request, 'index.html', context)

# Devuelve los datos de un post
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = { 'post': post }
    return render(request, 'detail.html', context)
