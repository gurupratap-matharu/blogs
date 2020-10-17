from django.shortcuts import get_object_or_404, render

from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    render(request, "blog/post_detail.html", {"post": post})
