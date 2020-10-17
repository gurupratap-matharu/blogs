from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView, ListView

from blog.forms import EmailPostForm
from blog.models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    template_name = "blog/post/list.html"
    context_object_name = "posts"


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


class PostShare(FormView):
    form_class = EmailPostForm
    template_name = "blog/post/share.html"
    success_url = "/thanks/"

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs["post_id"], status="published")
        uri = self.request.build_absolute_uri(post.get_absolute_url())
        self.success_url = post.get_absolute_url()
        form.send_email(title=post.title, uri=uri)
        return super().form_valid(form)
