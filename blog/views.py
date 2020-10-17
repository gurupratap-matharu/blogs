from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    template_name = "blog/post/list.html"
    context_object_name = "posts"


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
