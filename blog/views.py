from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    #Done in query : Sort according to published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # request - User input via Internet
    # blog/post_list.html : template file
    # {} : something for the template to use

    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
