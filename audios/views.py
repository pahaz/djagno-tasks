from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect

from audios.forms import UploadFileForm
from audios.models import Audio

from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Login/Logout

def index(request):
	audio_list = Audio.objects.order_by('id')
	context = RequestContext(request, {
		'audio_list': audio_list,
		'user': request.user,
	})
	return render(request, 'index.html', context)

def upload_file(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				# return HttpResponse("OK")
				# return HttpResponseRedirect(reverse('index'))
		else:
			form = UploadFileForm()
			# return HttpResponse("ERROR")
	return redirect('index')

def site_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
	return redirect('index')

def site_logout(request):
	logout(request)
	return redirect('index')

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def test(request):
	return HttpResponse(reverse('upload'))