from django.urls import path
from .views import Posts,PostDetails,PostComments,CommentDetails

urlpatterns=[
      path('posts/',Posts),
      path('posts/<int:pk>/',PostDetails),
      path('posts/<int:pk>/comments',PostComments),
      path('posts/<int:post_id>/comments/<int:pk>/',CommentDetails)
]

