from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Comment


def post_list(request):
	posts = Post.objects.all().order_by("-created_at")
	return render(request, "blog_app/post_list.html", {"posts": posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = post.comments.filter(is_approved=True)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect("post_detail", pk=post.pk)
	else:
		form = CommentForm()
	return render(request, "blog_app/post_detail.html", {"post": post, "comments": comments, "form": form})

def comment_list(request):
	comments = Comment.objects.all()
	return render(request, 'blog_app/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	return render(request, 'blog_app/comment_detail.html', {'comment': comment})
