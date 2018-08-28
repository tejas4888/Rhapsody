from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(label="comment_text",max_length=500)
