from django.urls import path
from . import views

app_name = 'micronutrients'

urlpatterns = [
    path('micronutrients/', views.MicronutrientList.as_view()),
    path('micronutrients/<slug:slug>/', views.MicronutrientDetail.as_view(), name="nutrient-page"),
    path('micronutrients/feedback/', views.NutrientFeedbackList.as_view()),
    path('micronutrients/feedback/<int:pk>/', views.NutrientFeedbackDetail.as_view()),
]