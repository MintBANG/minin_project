from django import forms
from reply.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nickname', 'contents', 'point_review')


