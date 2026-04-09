from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission

def submit(request):
    if request.method == "POST":
        user = request.POST.get("user")
        question_id = request.POST.get("question")
        choice_id = request.POST.get("choice")

        question = get_object_or_404(Question, id=question_id)
        choice = get_object_or_404(Choice, id=choice_id)

        Submission.objects.create(
            user=user,
            question=question,
            selected_choice=choice
        )

        return render(request, "result.html", {"choice": choice})

    return render(request, "submit.html")


def show_exam_result(request):
    submissions = Submission.objects.all()
    score = 0

    for submission in submissions:
        if submission.selected_choice.is_correct:
            score += 1

    return render(request, "result.html", {
        "score": score,
        "total": submissions.count()
    })