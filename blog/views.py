import logging

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm, EmailPostForm
from blog.models import Comment, Post

logger = logging.getLogger(__name__)


class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    template_name = "blog/post/list.html"
    context_object_name = "posts"


class PostDetailView(FormMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post/detail.html"
    success_message = "Comment added successfully!"
    form_class = CommentForm

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.save()
        messages.success(self.request, self.success_message)
        logger.info("saved comment with form %s", form)
        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(
            Post,
            slug=self.kwargs["post"],
            status="published",
            publish__year=self.kwargs["year"],
            publish__month=self.kwargs["month"],
            publish__day=self.kwargs["day"],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Post.comments.filter(active=True)
        return context


class PostShare(SuccessMessageMixin, FormView):
    form_class = EmailPostForm
    template_name = "blog/post/share.html"
    success_url = "/"
    success_message = "Post shared successfully!"

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs["post_id"], status="published")
        uri = self.request.build_absolute_uri(post.get_absolute_url())

        self.success_url = post.get_absolute_url()

        form.send_email(title=post.title, uri=uri)
        return super().form_valid(form)
