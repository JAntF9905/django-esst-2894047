from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView


# Create your views here.
from .models import Notes


class NotesListView(ListView):
    model = Notes
    template_name = "notes/notes_list.html"
    context_object_name = "notes"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


def detail(request, id):
    try:
        note = Notes.objects.get(id=id)
    except Notes.DoesNotExist:
        raise Http404("This note does not exist")
    return render(request, "notes/notes_detail.html", {"note": note})
