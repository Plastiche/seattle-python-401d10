from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required


@login_required
def note_list_view(request):
    notes = get_list_or_404(Note)
    context = {
        'notes': notes,
    }

    return render(request, 'notes/note_list.html', context)

@login_required
def note_detail_view(request, pk=None):
    note = get_object_or_404(Note, id=pk)
    context = {
        'note': note,
    }

    return render(request, 'notes/note_detail.html', context)
