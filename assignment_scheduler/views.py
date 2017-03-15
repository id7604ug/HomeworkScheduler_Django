from django.shortcuts import render, redirect
from .models import ScheduleItem
from .forms import AddAssignmentForm
from django.utils import timezone

def index(request):
    assignments_list = ScheduleItem.objects.all()
    assignments_due_today = assignments_list.filter(due_date=timezone.now().date())
    assignments_due_tomorrow = assignments_list.filter(due_date=(timezone.now() + timezone.timedelta(days=1)).date())
    assignments_past_due = assignments_list.filter(due_date__lt=timezone.now().date())
    print(len(assignments_past_due))
    return render(request, 'assignment_scheduler/index.html', {'due_today':assignments_due_today,'due_tomorrow':assignments_due_tomorrow,'past_due':assignments_past_due})

def assignment_list(request):
    assignments = ScheduleItem.objects.all()
    return render(request, 'assignment_scheduler/assignment_list.html', {'assignments': assignments})

def add_assignment(request):
    if request.method =="POST":
        form = AddAssignmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            assignment = ScheduleItem.objects.get(id=post.pk)
            return render(request, 'assignment_scheduler/read_one_assignment.html', {'assignment': assignment})
    else:
        form = AddAssignmentForm()
    return render(request, 'assignment_scheduler/add_assignment.html', {'form': form})

def assignment_read(request, id):
    assignment = ScheduleItem.objects.get(id=id)
    return render(request, 'assignment_scheduler/read_one_assignment.html', {'assignment':assignment})

def assignment_delete(request, id):
    ScheduleItem.objects.get(id=id).delete()
    assignments = ScheduleItem.objects.all()
    return redirect('/assignment_list/', {'assignments':assignments})

def check_due_assignments(request):
    return render(request, 'assignment_scheduler/check_due_assignments.html', {})

def assignment_complete(request, id):
    ScheduleItem.objects.get(id=id).complete = True

    assignments = ScheduleItem.objects.all()
    return redirect('/assignment_list/', {'assignments':assignments})
