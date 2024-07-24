from django import forms
from .models import Question, Answer, Category

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'question_text', 'marks']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'option_text', 'is_correct']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
