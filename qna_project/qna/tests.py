from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Question


class QuestionAPITest(APITestCase):
    def test_create_question(self):
        url = reverse('questions-list')
        data = {'text': 'Тестовый вопрос?'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 1)
