from . import views
from django.urls import path

urlpatterns=[
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('', views.UserProfile.as_view(), name='user_profile'),
    path('article/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    #path('add_post/', views.AddPost.as_view(), name='add_post'),

]