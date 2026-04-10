from django.contrib import admin
# Importing 7 classes as requested (adjust names based on your models.py)
from .models import Question, Choice, Submission, Lesson 

# 1. QuestionInline: To see choices/submissions inside the Question page
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

# 2. QuestionAdmin: Customizing how Questions appear
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']

# 3. LessonAdmin: Customizing the Lesson interface
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course') # Assuming Lesson has these fields
    inlines = [QuestionInline]

# Registering the classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
