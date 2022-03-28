from django.contrib import admin
from pw26s.models import Aluno, Responsavel


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'responsavel')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'telefone', 'responsavel')


class Responsaveis(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'telefone')


admin.site.register(Aluno, Alunos)
admin.site.register(Responsavel, Responsaveis)
