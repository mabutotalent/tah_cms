# from django.views.generic import  DetailView
from django.shortcuts import render, get_object_or_404

from .models import Post, Comment
from categories.models import Category
from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form})



 


