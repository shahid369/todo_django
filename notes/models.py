from django.db import models
from django.shortcuts import redirect,reverse
LABEL_CHOICES=(
    
    ('P','primary'),
    ('SE','secondary'),
    ('S','success'),
    ('DD','danger'),
    ('W','warning'),
    ('I','info'),
    ('L','light'),
    ('D','dark'),
    
)
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date=models.DateTimeField()
    label=models.CharField(choices=LABEL_CHOICES,max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_finish_item_url(self):
        return redirect(reverse("finished-note-item",kwargs={
            'id':self.id
        }))
    def get_recover_item_url(self):
        return redirect(reverse("recover-note-item",kwargs={
            'id':self.id
        }))
    def get_delete_item_url(self):
        return redirect(reverse("delete-note-item",kwargs={
            'id':self.id
        }))    