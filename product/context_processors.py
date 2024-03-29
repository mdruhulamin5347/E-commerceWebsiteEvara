from .models import Category

def category(request):
    cate = Category.objects.all()
    return {'cate':cate}