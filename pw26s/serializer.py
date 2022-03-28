from rest_framework import serializers
from pw26s.models import Aluno, Responsavel


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'telefone', 'responsavel']


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ['id', 'nome', 'email', 'telefone']
