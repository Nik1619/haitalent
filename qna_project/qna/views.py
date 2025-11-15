from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        if question_id:
            question = get_object_or_404(Question, id=question_id)
            return question.answers.all()
        return super().get_queryset()

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_id')
        if not question_id:
            raise ValidationError("Question ID is required to create an answer")
        question = get_object_or_404(Question, id=question_id)
        serializer.save(question=question)
