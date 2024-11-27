from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Post
from .forms import PostCreationForm
# Create your views here.
# @login_required
def dashboard(request):
    posts = Post.all()
    return render(request, 'dashboard.html', {'posts':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save
            return redirect('dashboard')
        else:
            form = PostCreationForm()
    return render(request, 'dashboard', {'form':form})