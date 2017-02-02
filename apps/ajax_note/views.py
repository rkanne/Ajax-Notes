from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Notes
from forms import NoteForm 
from django.views.generic import View
from django.core.urlresolvers import reverse

# Create your views here.
class Welcome(View):
	def get(self, request):
		notes = Notes.objects.all()
		context = {
			'notes': notes,
			'new_note_form': NoteForm(),
		}
		return render(request, 'ajax_note/index.html', context)

class Note(View):
	def get(self, request):
		context = {
	 		'notes': Notes.objects.all()
		}
		return render(request, 'ajax_note/note_partial.html', context)

	def post(self, request):
		add_note = Notes.objects.create(title=request.POST['title'])
		return redirect(reverse('notes'))


class Update(View):
	def get(self, request):
		return redirect(reverse('welcome'))

	def post(self, request):
		update = Notes.objects.update(request)
		return redirect(reverse('notes'))

class Delete(View):
	def get(self, request):
		return render(request, 'ajax_note/note_partial.html')


	def post(self, request):
		delete = Notes.objects.delete(request)
		return redirect(reverse('notes'))

