from django.shortcuts import render,get_object_or_404,redirect
from .models import Note
from .forms import NoteModelForm
# Create your views here.
def note_list_view(request):
    form=NoteModelForm()
    if request.method == 'POST':
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note-list")
    todo_list=Note.objects.filter(finished=False)
    finished_list=Note.objects.filter(finished=True)
    context={'todo_list':todo_list,
             'finished_list':finished_list,
             'form':form
             }
    return render(request,"note_list.html",context)

def finished_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.finished=True
    note.save()
    return redirect('note-list')

def recover_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.finished=False
    note.save()
    return redirect('note-list')

def delete_item(request,id):
    note=get_object_or_404(Note,id=id)
    note.delete()
    return redirect('note-list')