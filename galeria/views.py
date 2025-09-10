from django.shortcuts import render, get_object_or_404
from galeria.models import Imagem


def index(request):
    fotografias = Imagem.objects.all()
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Imagem, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
