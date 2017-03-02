from django.shortcuts import render, redirect
from .models import ScheduleItem
from .forms import AddAssignmentForm

# Create your views here.

def assignment_list(request):
    assignments = ScheduleItem.objects.all()
    return render(request, 'assignment_scheduler/assignment_list.html', {'assignments': assignments})

def index(request):
    return render(request, 'assignment_scheduler/index.html', {})

def add_assignment(request):
    if request.method =="POST":
        form = AddAssignmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('assignment_detail', pk=post.pk)
    else:
        form = AddAssignmentForm()
    return render(request, 'assignment_scheduler/add_assignment.html', {'form': form})
