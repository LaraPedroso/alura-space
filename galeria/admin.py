from django.contrib import admin
from galeria.models import Imagem

class listaImagens(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda','descricao', 'categoria', 'foto', 'publicada')
    list_editable = ('publicada',)
    list_display_links = ('id', 'nome', 'descricao' )
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome',)
    



admin.site.register(Imagem, listaImagens)
