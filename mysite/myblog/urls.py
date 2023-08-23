from . import views
from django.urls import path

urlpatterns=[
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('article/<int:pk>', views.PostDetail.as_view(), name='post_detail'),

]