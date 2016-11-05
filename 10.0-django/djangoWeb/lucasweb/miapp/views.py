from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
'''Agregado.....'''
from django.http import HttpResponse
from .models import Choice, Question
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'miapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'miapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'miapp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'miapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('miapp:results', args=(question.id,)))

def boostrap(request):
    return render(request, 'miapp/boostrap.html')

def boostrap2(request):
    return render(request, 'miapp/boostrap2.html')

def image(request, contact_id, file_name):
    return HttpResponse('<img src="%s" />' % file_name)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'miapp/index.html', context)

#from django.template import loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'miapp/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'miapp/results.html', {'question': question})
