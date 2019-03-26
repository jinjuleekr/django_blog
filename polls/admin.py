from django.contrib import admin
from polls.models import Question,Choice

# Question 및 Choice 한 화면에서 변경하기
# class ChoiceInline(admin.StackedInline):
# 관리페이지 테이블 형태로 보여주기
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1
	
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				 {'fields':['question_text']}),
		('Date information', {'fields':['pub_date'], 'classes':['collapse']}), #화면 접기
	]
	inlines = [ChoiceInline]						# Choice 모델 클래스 같이 보기
	list_display = ('question_text', 'pub_date')	# 레코드 리스트 컬럼 지정 
	list_filter = ['pub_date']						# 필터 사이드 바 추가
	search_fields = ['question_text']				# 검색 박스 추가


	

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


