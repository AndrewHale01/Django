from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
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

def favorites(request):
    favorite_ids = request.session.get('favorite_courses', [])
    courses = Course.objects.filter(id__in=favorite_ids)
    return render(request, 'products/favorites.html', {'courses': courses})

@require_http_methods(["POST"])
def toggle_favorite(request, pk):
    get_object_or_404(Course, pk=pk)
    favorite_ids = request.session.get('favorite_courses', [])
    if pk in favorite_ids:
        favorite_ids.remove(pk)
    else:
        favorite_ids.append(pk)
    request.session['favorite_courses'] = favorite_ids
    request.session.modified = True
    return redirect(request.POST.get('next', 'index'))

@require_http_methods(["POST"])
def add_to_cart(request, pk):
    get_object_or_404(Course, pk=pk)
    cart_ids = request.session.get('cart_courses', [])
    if pk not in cart_ids:
        cart_ids.append(pk)
    request.session['cart_courses'] = cart_ids
    request.session.modified = True
    return redirect(request.POST.get('next', 'index'))

@require_http_methods(["POST"])
def remove_from_cart(request, pk):
    cart_ids = request.session.get('cart_courses', [])
    if pk in cart_ids:
        cart_ids.remove(pk)
        request.session['cart_courses'] = cart_ids
        request.session.modified = True
    return redirect(request.POST.get('next', 'index'))

@require_http_methods(["GET"])
def cart(request):
    cart_ids = request.session.get('cart_courses', [])
    courses = Course.objects.filter(id__in=cart_ids)
    return render(request, 'products/cart.html', {'courses': courses})

@require_http_methods(["POST"])
def clear_cart(request):
    request.session['cart_courses'] = []
    request.session.modified = True
    return redirect('cart')

@require_http_methods(["POST"])
def checkout(request):
    if not request.session.get('cart_courses', []):
        return redirect('cart')
    request.session['cart_courses'] = []
    request.session.modified = True
    return render(request, 'products/checkout_success.html')

def about(request):
    return render(request, 'products/about.html')

def admin_panel(request):
    if not request.user.is_staff:
        return redirect('index')
    
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'products/admin_panel.html', {'courses': courses})

@require_http_methods(["GET", "POST"])
def course_add(request):
    if not request.user.is_staff:
        return redirect('index')
    
    if request.method == 'POST':
        course = Course.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            image=request.POST.get('image')
        )
        return redirect('admin_panel')
    return render(request, 'products/course_form.html')

@require_http_methods(["GET", "POST"])
def course_edit(request, pk):
    if not request.user.is_staff:
        return redirect('index')
    
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.title = request.POST.get('title')
        course.description = request.POST.get('description')
        course.price = request.POST.get('price')
        course.image = request.POST.get('image')
        course.save()
        return redirect('admin_panel')
    return render(request, 'products/course_form.html', {'course': course})

@require_http_methods(["POST"])
def course_delete(request, pk):
    if not request.user.is_staff:
        return redirect('index')
    
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('admin_panel')
