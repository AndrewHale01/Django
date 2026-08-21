from .models import Course
from decimal import Decimal


def shopping_data(request):
    favorite_ids = request.session.get('favorite_courses', [])
    cart_ids = request.session.get('cart_courses', [])
    cart_items = Course.objects.filter(id__in=cart_ids)
    return {
        'favorite_course_ids': favorite_ids,
        'favorite_count': len(favorite_ids),
        'cart_courses': cart_items,
        'cart_count': len(cart_ids),
        'cart_total': sum((course.price for course in cart_items), Decimal('0')),
    }