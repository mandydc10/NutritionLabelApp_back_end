from django.urls import path
from . import views

urlpatterns = [
    path('wholefoods/', views.WholefoodList.as_view()),
    path('wholefoods/<slug:slug>/', views.WholefoodDetail.as_view()),
    path('wholefoods/feedback/', views.WholefoodFeedbackList.as_view()),
    path('wholefoods/feedback/<int:pk>/', views.WholefoodFeedbackDetail.as_view()),
]