from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class NoteDeleteView(DeleteView):
    model = Notes
    template_name = 'app_notes/delete_note_form.html'
    success_url = reverse_lazy('home1')


class NoteUpdateView(UpdateView):
    model = Notes
    template_name = 'app_notes/update_note_form.html'
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('home1')


class NotesCreateView(CreateView):
    model = Notes
    template_name = 'app_notes/create_note_form.html'
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('home1')


class NotesListView(ListView):
    model = Notes
    template_name = 'app_notes/home.html'
    context_object_name = 'notes'


def home(request):
    note = Notes.objects.all()
    return render(request, 'app_notes/home.html', {'notes': note})
