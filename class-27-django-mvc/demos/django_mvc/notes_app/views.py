from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Note


def note_detail_view(request, pk=None):
    """
    """
    context = {
        'note': get_object_or_404(Note, id=pk)
    }

    return render(request, 'notes/note_detail.html', context)


def note_list_view(request):
    """
    """
    context = {
        'notes': get_list_or_404(Note)
    }

    return render(request, 'notes/note_list.html', context)
