from product.models import Category


def subject_render(request):
    context = {
        'context_categories': Category.objects.filter(is_parent=True)
        
    }
    return context