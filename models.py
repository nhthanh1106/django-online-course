from django.db import models

class Question(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    def __str__(self): return self.question_text
    def is_get_score(self, selected_ids):
        all_choices = self.choice_set.all()
        return all_choices.filter(id__in=selected_ids, is_correct=True).count() == all_choices.filter(is_correct=True).count()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self): return self.choice_text

class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
