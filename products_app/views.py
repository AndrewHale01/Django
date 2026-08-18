from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'products/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    history = request.session.get('viewed_courses', [])
    if pk not in history:
        history.append(pk)
        request.session['viewed_courses'] = history
        request.session.modified = True
        
    return render(request, 'products/course_detail.html', {'course': course})

def view_history(request):

    history_ids = request.session.get('viewed_courses', [])
    viewed_courses = Course.objects.filter(id__in=history_ids)
    return render(request, 'products/view_history.html', {'courses': viewed_courses})
