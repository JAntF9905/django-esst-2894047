from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Note

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        raise Http404('This note does not exist')
    return render(request, 'notes/notes_detail.html', {'note': note})

