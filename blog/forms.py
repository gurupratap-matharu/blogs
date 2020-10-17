from django import forms
from django.core.mail import send_mail


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def send_email(self, post):
        from_name = self.cleaned_data["name"]
        from_email = self.cleaned_data["email"]
        to_email = self.cleaned_data["to"]
        comments = self.cleaned_data["comments"]

        subject = "{0} recommends you read {1}".format(from_name, post.title)
        message = "Read {0} at {1}\n{2}'s comments: {3}".format(
            post.title,
            post.get_absolute_url(),
            from_name,
            comments,
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[to_email],
            fail_silently=False,
        )
