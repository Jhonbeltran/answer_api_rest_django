from rest_framework import generics
from .models import Answer
from .serializers import AnswerSerializer
from django.shortcuts import get_object_or_404

class AnswerList(generics.ListCreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk']
			)
		return obj
