from django.http import HttpResponse
from django.shortcuts import render

def home(request):

	#return HttpResponse('hello')
	return render(request,'home.html')

def count(request):
	txt = request.GET['utext']
	txt1 = txt.split()
	txtwordcount = {}

	for i in txt1:
		if i not in txtwordcount:
			txtwordcount[i]=1
		else:
			txtwordcount[i]=txtwordcount[i]+1
	#print(txt)
	fulltext = {
		'txt':txt,
		'length':len(txt1),
		'repeat':txtwordcount
	}
	return render(request,'count.html',fulltext)
