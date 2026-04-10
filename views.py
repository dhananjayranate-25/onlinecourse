from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Submission

def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Save the submission for the user
        Submission.objects.create(
            user=request.user, 
            question=question, 
            selected_choice=selected_choice
        )
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return redirect('polls:show_exam_result', question_id=question.id)

def show_exam_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # You might want to calculate total score or just show the choice picked
    submissions = Submission.objects.filter(question=question, user=request.user)
    
    return render(request, 'polls/results.html', {
        'question': question,
        'submissions': submissions
    })
