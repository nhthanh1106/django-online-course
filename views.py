def submit(request, course_id):
    if request.method == 'POST':
        question_ids = request.POST.getlist('question_ids')
        choices = request.POST.getlist('choices')
        # Logic associate submission here
        return render(request, 'exam_result_bootstrap.html')

def show_exam_result(request, course_id, submission_id):
    submission = Submission.objects.get(id=submission_id)
    total_score = 0
    for question in submission.enrollment.course.question_set.all():
        if question.is_get_score(submission.choices.all()):
            total_score += 1
    return render(request, 'exam_result_bootstrap.html', {'total_score': total_score})
