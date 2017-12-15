from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.db.models.functions import Coalesce
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by( Coalesce('published_date','title').desc() )
    return render(request, 'blog/post_list.html', {'posts' : posts} )
