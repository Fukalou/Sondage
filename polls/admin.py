from django.contrib import admin

from polls.models import Question, Choice, Sondage


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['question_text']}),
        ('Information de la date',  {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class SondageAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Sondage, SondageAdmin)