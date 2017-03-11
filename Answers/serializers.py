from .models import Answer
from rest_framework import serializers

class AnswerSeralizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Answer
		fields = ('id', 
				  'change_pass_answer', 
				  'relation_answer', 
				  'personal_answer', 
				  'pay_method_answer', 
				  'age_answer')

