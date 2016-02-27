from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
	posts = Post.objects.all()#filter(published_data__lte=timezone.now()).order_by('published_data')
	a = 2
	return render(request, "blog/post_list.html",{"posts":posts, "a":a})
