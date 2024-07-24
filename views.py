from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
import random
import uuid

def home(request):
    context = {'categories': Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', context)

def quiz(request):
    category = request.GET.get('category', '')
    context = {'category': category}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs = list(question_objs)

        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "uid": str(question_obj.uid),
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'message': str(e)})

def submit_quiz(request):
    if request.method == 'POST':
        try:
            data = request.POST
            score = 0
            total_marks = 0

            for key in data.keys():
                if 'question' in key:
                    question_uid = key.split('_')[1]
                    answer_uid = data[key]

                    question = Question.objects.get(uid=uuid.UUID(question_uid))
                    total_marks += question.marks
                    answer = Answer.objects.get(uid=uuid.UUID(answer_uid))

                    if answer.is_correct:
                        score += question.marks

            context = {
                'score': score,
                'total_marks': total_marks,
                'status': 'Success' if score > 0 else 'Try Again'
            }
            return render(request, 'results.html', context)

        except Exception as e:
            print(e)
            return render(request, 'results.html', {'status': 'Error', 'message': str(e)})

    return HttpResponse("Invalid request")

def add_question(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        question_text = request.POST.get('question')
        marks = request.POST.get('marks')

        category, created = Category.objects.get_or_create(category_name=category_name)
        question = Question.objects.create(
            category=category,
            question=question_text,
            marks=marks
        )

        answers = request.POST.getlist('answers')
        is_correct_list = request.POST.getlist('is_correct')

        for answer_text, is_correct in zip(answers, is_correct_list):
            Answer.objects.create(
                question=question,
                answer=answer_text,
                is_correct=bool(int(is_correct))
            )

        return redirect('home')

    return render(request, 'add_question.html')
