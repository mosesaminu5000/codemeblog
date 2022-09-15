from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import post, Category


def detail(request, slug):
    post = get_object_or_404(post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =post
            comment.save()
            
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/detail.html', {'post':post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    return render(request, 'blog/category.html', {'category': category})
