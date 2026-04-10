from django.urls import path
from . import views

# Setting the app name for namespacing (optional but recommended)
app_name = 'polls'

urlpatterns = [
    # ... your other paths like index or detail ...

    # Path for the submit function
    # Example URL: /polls/5/submit/
    path('<int:question_id>/submit/', views.submit, name='submit'),

    # Path for the show_exam_result function
    # Example URL: /polls/5/results/
    path('<int:question_id>/results/', views.show_exam_result, name='show_exam_result'),
]
