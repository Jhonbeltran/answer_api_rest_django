from django.db import models

class Answer(models.Model):
	change_pass_answer = models.IntegerField()
	relation_answer = models.CharField(max_length=255)
	personal_answer = models.CharField(max_length=255)
	pay_method_answer = models.CharField(max_length=255)
	age_answer = models.IntegerField()
