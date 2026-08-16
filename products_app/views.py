from django.http import Http404
from django.shortcuts import render

courses = [
    {'id': 1, 'title': 'Python for Beginners', 'description': 'Learn Python from scratch.', 'price': 49.99, 'image': 'https://m.media-amazon.com/images/I/317ToGD2FRL._SX342_SY445_ML2_.jpg'},
    {'id': 2, 'title': 'Django Web Development', 'description': 'Build web applications using Django.', 'price': 79.99, 'image': 'https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1659231847i/61790506.jpg'},
    {'id': 3, 'title': 'Data Science with Python', 'description': 'Analyze data and build machine learning models.', 'price': 99.99, 'image': 'https://www.wiley.com/storefront-pdp-assets/_next/image?url=https%3A%2F%2Fmedia.wiley.com%2Fproduct_data%2FcoverImage300%2F68%2F11195268%2F1119526868.jpg&w=640&q=75'},
]

def course_list(request):
    return render(request, 'products/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = next((c for c in courses if c['id'] == pk), None)
    if course is None:
        raise Http404('Course not found')
    return render(request, 'products/course_detail.html', {'course': course})