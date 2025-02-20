

from django.urls import path
from .views import blog, bloges, createblog, updateBlog, deleteBlog, deleteArea, createarea, commentView, deleteComment

urlpatterns = [
    path('blog/', blog),
    path('bloges/', bloges),
    path('create/', createblog),
    path('update/<int:id>/', updateBlog),
    path('delete/<int:id>/', deleteBlog),
    path('delete_area /<int:id>/', deleteArea, name='area'),
    path('area/',  createarea),
    path('comment/<int:id>/', commentView, name='comment_view'),
    path('delete_comment/<int:id>/', deleteComment, name='delete_comment'),

]

