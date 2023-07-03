from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import Q
from .models import Tag


@csrf_exempt
def add_tag(request):
    if request.method == 'POST':
        print(request.POST)  
        uid = request.POST['uid']
        Tag.objects.create(uid=uid)
        return JsonResponse({'message': 'Tag added successfully.'})

@csrf_exempt
def tag_detail(request, uid):
    tag = get_object_or_404(Tag, uid=uid)
    if request.method == 'POST':
        tag.name = request.POST['name']
        tag.description = request.POST['description']
        tag.save()
        return HttpResponseRedirect(reverse('rfid_app:index'))
    else:
        return render(request, 'rfid_app/tag_detail.html', {'tag': tag})
    
@csrf_exempt
def delete_tag(request, uid):
    tag = get_object_or_404(Tag, uid=uid)
    tag.delete()
    return HttpResponseRedirect(reverse('rfid_app:index'))

@csrf_exempt
def tag_detail(request, uid):
    tag = get_object_or_404(Tag, uid=uid)
    if request.method == 'POST':
        tag.name = request.POST['name']
        tag.description = request.POST['description']
        tag.price = request.POST['price']  # 添加这行
        tag.save()
        return HttpResponseRedirect(reverse('rfid_app:index'))
    return render(request, 'rfid_app/tag_detail.html', {'tag': tag})

def index(request):
    tags = Tag.objects.order_by('-timestamp')
    context = {'tags': tags}
    return render(request, 'rfid_app/index.html', context)

def search(request):
    query = request.GET.get('q')
    if query:
        tags = Tag.objects.filter(
            Q(uid__icontains=query) | 
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )
    else:
        tags = Tag.objects.all()
    return render(request, 'rfid_app/search.html', {'tags': tags})