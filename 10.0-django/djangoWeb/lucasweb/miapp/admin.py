from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Contact
#https://www.djangosnippets.org/snippets/934/
#http://www.psychicorigami.com/2009/06/20/django-simple-admin-imagefield-thumbnail/
#https://docs.djangoproject.com/es/1.10/ref/contrib/admin/actions/

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

from .image_widget import AdminImageWidget
from django import forms

# class FileUploadForm(forms.ModelForm):
#     upload = forms.FileField(widget=AdminImageWidget)
#     class Meta:
#         model = Contact
#         fields = '__all__'
class FileUploadAdmin(admin.ModelAdmin):
    # form = FileUploadForm
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'photo':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(FileUploadAdmin,self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Contact, FileUploadAdmin)

# class AdminImageWidget(AdminFileWidget):
#     def render(self, name, value, attrs=None):
#         output = []
#         if value and getattr(value, "url", None):
#             image_url = '../media/'+ value.url
#             file_name=str(value)
#             output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
#                 (image_url, image_url, file_name, _('Change:')))
#         output.append(super(AdminFileWidget, self).render(name, value, attrs))
#         return mark_safe(u''.join(output))

# fieldsets = (
#     (None, {
#         'fields': ('url', 'title', 'content', 'sites')
#     }),
#     ('Advanced options', {
#         'classes': ('collapse',),
#         'fields': ('registration_required', 'template_name'),
#     }),
# )
