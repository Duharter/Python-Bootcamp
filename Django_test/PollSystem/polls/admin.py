from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Poll System Admin"
admin.site.site_title = "Poll System Admin Area"
admin.site.index_title = "Welcome to the Poll System Admin Area"
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
