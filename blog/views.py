from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post


@login_required
def personal_feed(request):
    user = request.user
    posts = Post.objects.filter(blog__in=user.subscriptions.all()).exclude(read_by=user).order_by('-created')
    return render(request, 'blog/feed.html', {'posts': posts})
