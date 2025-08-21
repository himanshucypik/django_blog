from django.urls import path
from . import views

urlpatterns = [
	path("", views.post_list, name="post_list"),
	path("post/<int:pk>/", views.post_detail, name="post_detail"),
	# 👇 New routes for comments
	path('comments/', views.comment_list, name='comment_list'),
	path('comments/<int:pk>/', views.comment_detail, name='comment_detail'),
]