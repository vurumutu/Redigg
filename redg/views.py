from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.conf import settings


from .models import Comment, CommentThread, Finding

# Create your views here.
def show_finding(request, finding_id):
	response = "Finding id " + str(finding_id)
	return HttpResponse(response)

def index(request):
	findings_list = Finding.objects.all()
	template = loader.get_template('finding_page_template.html')
	context = {
		'findings_list': findings_list,
		'media_url':settings.MEDIA_URL,
	}
	return HttpResponse(template.render(context, request))

