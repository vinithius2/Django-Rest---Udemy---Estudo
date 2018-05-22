from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # Filtragem usando o Search Filter
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha01')
    # Por padrão é feito a busca por ID, é possível mudar, porém tem que ser campos UNIQUE para evitar problemas.
    # lookup_field = 'nome'

    # Filtragem de maneira manual, existe o django_filter que é usado no app Atracoes
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    ''''
    # Sobreescrevendo a action de GET
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
        # return Response({'teste': 123})

    # Sobreescrevendo a action de POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    # Sobreescrevendo a action de DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # Sobreescrevendo a action de GET com recurso
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # Sobreescrevendo a action de PUT
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # Sobreescrevendo a action de PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # Action personalizada Ex: http://127.0.0.1:8000/pontoturistico/1/denunciar/
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    # Action personalizada Ex: http://127.0.0.1:8000/pontoturistico/teste/
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
    '''
