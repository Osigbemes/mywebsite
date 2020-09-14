from django.shortcuts import render
from multimedia.models import Multimedia


def multimedia_index(request):
    media = Multimedia.objects.all()
    context={
        'media':media
    }
    return render(request, 'multimedia_index.html', context)

def multimedia_detail(request, pk):
    media = Multimedia.objects.get(pk=pk)
    context = {
        'media': media
    }
    return render(request, 'multimedia_detail.html', context)
