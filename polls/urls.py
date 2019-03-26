from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
	path('thanks/', views.thanks, name="thanks"),
	path('your-name/', views.get_name, name='name'),
	path('contact/', views.get_contact, name='contact'),
	path('', views.IndexView.as_view(), name='index'), # /polls/ 
	path('<int:pk>/',views.DetailView.as_view(), name='detail'), # /polls/5/
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # /polls/5/result
	path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/5/vote/
]