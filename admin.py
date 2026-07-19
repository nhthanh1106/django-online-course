from django.contrib import admin
# Cần import đủ 7 class này
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Implement các class yêu cầu
class QuestionInline(admin.StackedInline):
    model = Question

class ChoiceInline(admin.StackedInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Đăng ký admin để AI quét ra nội dung trong screenshot
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
