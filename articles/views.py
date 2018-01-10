from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Article 
# Create your views here.
def articles_create(request):
	return HttpResponse("<h1> Create </h1>")

def articles_detail(request, article_id):
	thing = Article.objects.get(id=article_id)
	context = {
		"thing":thing
	}
	return render(request, 'detail.html', context)

def articles_update(request):
	return HttpResponse("<h1> Update </h1>")

def articles_list(request):
	object_list= Article.objects.all()
	info = {
			"feed": object_list
		}
	return render(request, 'home.html', info)
	

def articles_delete(request):
	return HttpResponse("<h1> Delete </h1>")