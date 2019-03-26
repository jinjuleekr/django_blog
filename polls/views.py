from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Question, Choice
from django.views.generic import ListView, DetailView, View
import logging
from .forms import NameForm, ContactForm 
logger = logging.getLogger(__name__)

#--- Class-based GenericView
class IndexView(ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		""" 최근 생성된 질문 5개를 반환함 """
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(DetailView):
	model = Question
	template_name = "polls/results.html"

#---Function-based View	
def vote(request, question_id):
	logger.info("vote().question_id: %s" % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		#설문 투표 폼을 다시 보여준다.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# POST 데이터를 정상적으로 처리하였으면,
		# 항상 HttpResponseRedirectf를 반환하여 리다이렉션 처리함
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

############# class형으로 변환하면서 쓰이지 않음 (시작) #############
def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question':question})

		
def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

############# class형으로 변환하면서 쓰이지 않음 (끝) #############

def thanks(request):
	return render(request, 'polls/thanks.html')

def get_name(request):
	# POST 방식이면, 데이터가 담긴 제출된 폼으로 간주합니다.
	if request.method == 'POST':
		# request에 담긴 데이터로, 클래스 폼을 생성합니다.
		form = NameForm(request.POST)
		# 폼에 담긴 데이터가 유효한지 체크합니다.
		if form.is_valid():
			# 폼 데이터가 유효하면, 데이터는 cleaned_data로 복사됩니다.
			new_name = form.cleaned_data['your_name']
			# 로직에 따라 추가적인 처리를 합니다.

			# 새로운 URL로 리다이렉션시킵니다.
			return HttpResponseRedirect('/polls/thanks/')
		else:
			return HttpResponseRedirect('/')

	# POST 방식이 아니면(GET 요청),
	# 빈 폼을 사용자에게 보여줍니다.
	else:
		form = NameForm()

	return render(request, 'polls/name.html', {'form':form})

def get_contact(request):
	# POST 방식이면, 데이터가 담긴 제출된 폼으로 간주합니다.
	if request.method == 'POST':
		# request에 담긴 데이터로, 클래스 폼을 생성합니다.
		form = ContactForm(request.POST)
		# 폼에 담긴 데이터가 유효한지 체크합니다.
		if form.is_valid():
			# 폼 데이터가 유효하면, 데이터는 cleaned_data로 복사됩니다.
			new_subject = form.cleaned_data['subject']
			new_message = form.cleaned_data['message']
			# 로직에 따라 추가적인 처리를 합니다.

			# 새로운 URL로 리다이렉션시킵니다.
			return HttpResponseRedirect('/polls/thanks/')
		else:
			return HttpResponseRedirect('/')

	# POST 방식이 아니면(GET 요청),
	# 빈 폼을 사용자에게 보여줍니다.
	else:
		form = ContactForm()

	return render(request, 'polls/contact.html', {'form':form})


