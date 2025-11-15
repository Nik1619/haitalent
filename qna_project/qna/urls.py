from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<int:question_id>/answers/', AnswerViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='answers-list-create'),
    path('answers/<int:pk>/', AnswerViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    }), name='answer-detail'),
]
