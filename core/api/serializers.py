from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracoesSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa_01 = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado',
            'atracoes', 'comentarios', 'avaliacoes',
            'endereco', 'foto', 'descricao_completa_01',
            'descricao_completa_02',
        )

    def get_descricao_completa_01(self, obj):
        return '{0} - {1}'.format(obj.nome, obj.descricao)
