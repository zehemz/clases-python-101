from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Contact


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

# fieldsets = (
#     (None, {
#         'fields': ('url', 'title', 'content', 'sites')
#     }),
#     ('Advanced options', {
#         'classes': ('collapse',),
#         'fields': ('registration_required', 'template_name'),
#     }),
# )

#admin.site.register(Contact, ContactAdmin)
#admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
# Register your models here.
