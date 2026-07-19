from django.shortcuts import render

# Phải có đúng 2 hàm này
def submit(request, course_id):
    return render(request, 'submit.html')

def show_exam_result(request, course_id, submission_id):
    return render(request, 'exam_result.html')
