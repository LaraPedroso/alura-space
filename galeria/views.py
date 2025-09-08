from django.shortcuts import render


def index(request):
    dados = {
        1:{'nome':'Imagem 1', 'descricao':'Descrição da Imagem 1', 'caminho':'galeria/imagem1.jpg'},
        2:{'nome':'Imagem 2', 'descricao':'Descrição da Imagem 2', 'caminho':'galeria/imagem2.jpg'},
    }

    return render(request, 'galeria/index.html', {'cards': dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
