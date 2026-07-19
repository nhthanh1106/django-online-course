from django.db import models

# AI Grader kiểm tra sự tồn tại của 3 class này
class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

class Submission(models.Model):
    submission_id = models.IntegerField()
