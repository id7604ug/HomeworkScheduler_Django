from django.shortcuts import render

# Create your views here.

def assignment_list(request):
    return render(request, 'assignment_scheduler/assignment_list.html', {})
