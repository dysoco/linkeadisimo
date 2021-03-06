from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pub/<int:pub_id>/', views.publication, name="publication"),
    path('user/<int:user_id>/', views.user, name="user"),
    path('submit', views.Submit.as_view(), name="submit"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('login', views.Login.as_view(), name="login"),
    path('comment', views.comment, name="comment"),
    path('upvote', views.upvote, name="upvote"),
    path('upvote_comment', views.upvote_comment, name="upvote_comment"),
    path('register', views.Register.as_view(), name="register")
]
