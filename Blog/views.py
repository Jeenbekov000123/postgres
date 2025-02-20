from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Area , Comment
from .forms import BlogForm, UpdateBlogForm, UpdateAreaForm,CreateCommentForm


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'blog.html', context)


def bloges(request):
    bloges = Blog.objects.first()
    context = {'bloges': bloges}
    return render(request, 'bloges.html', context)


def createblog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        Blog.objects.create(title=title, body=body)
        return redirect('http://127.0.0.1:8000/blog/')  # Используем имя маршрута

    form = BlogForm()
    context = {'form': form}
    return render(request, 'form_blog.html', context)


def updateBlog(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')  # Используем имя маршрута

        return HttpResponse('Ошибка при обновлении данных')

    form = UpdateBlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'updateBlog.html', context)


def deleteBlog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/blog/')  # Используем имя маршрута вместо жесткого URL


def createarea(request):
    if request.method == 'POST':
        title = request.POST.get('name')
        body = request.POST.get('about')

        Blog.objects.create(title=title, body=body)
        return redirect('http://127.0.0.1:8000/blog/')  # Используем имя маршрута

    form = BlogForm()
    context = {'form': form}
    return render(request, 'Area.html', context)


def updateArea(request, id):
    area = get_object_or_404(Area, pk=id)






    if request.method == 'POST':
        form = UpdateAreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('home')

        return HttpResponse('Ошибка при обновлении данных')

    form = UpdateAreaForm(instance=area)
    context = {'form': form}
    return render(request, 'updateArea.html', context)


def deleteArea(request, id):
    area = Area  .objects.get(Area, pk=id)
    area.delete()
    return redirect('Area')

def commentView(request,id):
    if request.method == "POST":
        author = request.POST['author']
        text = request.POST['text']
        blog = Blog.objects.get(id=id)
        Comment.objects.create(
            blog=blog,
            author=author,
            text=text


        )

    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    form = CreateCommentForm()
    context = {
        'id': id,
        'form': form,
        'comments': comments
    }
    return render(request,'comment.html', context)


def deleteComment(request, id):
    comment = Comment.objects.get(id=id)



    blog_id = comment.blog.id
    comment.delete()
    return redirect('comment_view', id=blog_id)