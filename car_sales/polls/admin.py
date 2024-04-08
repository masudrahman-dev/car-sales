from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')



def site():
    return None
