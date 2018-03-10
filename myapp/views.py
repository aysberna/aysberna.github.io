from django.shortcuts import render, render_to_response

# Create your views here.
def index (request):
	return render_to_response('index.html')

def muhur (request):
	return render_to_response('muhur.html')

def tablo (request):
	return render_to_response('tablo.html')

def video (request):
	return render_to_response('video.html')

def stickeretiket (request):
	return render_to_response('stickeretiket.html')

def kese (request):
	return render_to_response('kese.html')
	
def kagitip (request):
	return render_to_response('kagitip.html')
