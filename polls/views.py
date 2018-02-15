from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from polls.forms.login import LoginForms
from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Vous n'avez pas choisi de réponse !",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class LoginView(generic.FormView):
    template_name = 'polls/login.html'
    form_class = LoginForms
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if username is None:
            form.add_error('username',
                           'Username vide ')
            return super(LoginView, self).form_invalid(form)


        user = authenticate(username=username,
                            password=password)
        if user is None:
            form.add_error(None,
                           'Erreur de connexion')
        return super(LoginView, self).form_valid(form)

        login(self.request, user)

class InscriptionView(generic.FormView):
    template_name = 'polls/inscription.html'
    form_class = LoginForms
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if username is None:
            form.add_error('username',
                           'Username vide ')
            return super(LoginView, self).form_invalid(form)


        user = authenticate(username=username,
                            password=password)
        if user is None:
            form.add_error(None,
                           'Erreur de connexion')
        return super(LoginView, self).form_valid(form)

        login(self.request, user)