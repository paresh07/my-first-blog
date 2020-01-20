from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        '''All the fields from the form are now in request.POST(as POST method is used in form)
        in above line:If method is POST then we want to construct the PostForm with data from the form'''
        if form.is_valid():
            post = form.save(commit=False)  #commit=False means that we don't want to save the Post model yet – we want to add the author first.
            post.author = request.user    #we add an author (since there was no author field in the PostForm and this field is required
            post.published_date = timezone.now()
            post.save()    #post.save() will preserve changes (adding the author) and a new blog post is created!
            return redirect('post_detail', pk=post.pk)      #redirect to new page & post_detail is the name of the func in view
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})       #{} tell django which template to use

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)        #when we create a form, we pass this post as an instance
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)          ##when we create a form, we pass this post as an instance
    return render(request, 'blog/post_edit.html', {'form': form})