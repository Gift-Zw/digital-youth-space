from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 45, 'rows': 4, 'placeholder': 'Comment'}))
