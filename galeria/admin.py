from django.contrib import admin
from galeria.models import Imagem

class listaImagens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda','descricao', 'categoria', 'foto')
    list_display_links = ('id', 'nome', 'descricao' )
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 10



admin.site.register(Imagem, listaImagens)
