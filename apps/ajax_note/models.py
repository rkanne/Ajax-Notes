from __future__ import unicode_literals
from django.db import models

class NotesManager(models.Manager):
	def add(self, name):
		note_message =[]
		if len(name) == 0:
			note_message.append("Note is required")
		else:
			note_message.append("*** You have added your note!!! ***")
			return (True, note_message)

	def delete(self, request):
		print "Click delete button"
		self.filter(id=request.POST['id']).delete()
		print request.POST['id']
		return (True, "Your note has deleted")

	def update(self, request):
		print "inside update function"
		self.filter(id=request.POST['id']).update(description=request.POST['description'])
		return (True, "Your description has updated")

class Notes(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = NotesManager()

		
