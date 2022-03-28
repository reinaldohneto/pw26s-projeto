from rest_framework import viewsets
from pw26s.models import Aluno, Responsavel
from pw26s.serializer import AlunoSerializer, ResponsavelSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class ResponsaveisViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
