from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from item.models import Item

@login_required
def index(request):
    items = Item.objects.filter(createdBy = request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

