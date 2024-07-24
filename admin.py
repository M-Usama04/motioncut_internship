from django.contrib import admin
from .models import Category, Question, Answer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'marks')
    search_fields = ('question',)
    list_filter = ('category',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question', 'is_correct')
    search_fields = ('answer',)
    list_filter = ('is_correct',)
