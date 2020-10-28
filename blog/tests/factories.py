import factory
from blog.models import Post
from users.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("catch_phrase")
    slug = factory.LazyAttribute(lambda a: "-".join(a.title.split()))
    author = factory.SubFactory(UserFactory)
    body = factory.Faker("text")
    status = "published"
