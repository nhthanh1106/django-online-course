from django.urls import path
from . import views

# Phải có đúng 2 path này
urlpatterns = [
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
