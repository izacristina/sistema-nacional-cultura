import pytest

from model_mommy import mommy

from gestao.views import diligencia_documental


@pytest.mark.django_db
def test_diligencia_documental(client):

    plano_cultura = mommy.make('PlanoCultura')
    plano_trabalho = mommy.make('PlanoTrabalho', plano_cultura=plano_cultura)
    user = mommy.make('Usuario', plano_trabalho=plano_trabalho)
    etapa = 'plano_cultura'
    st = 'situacao_lei_plano_id'

    request = client.get('/gestao/diligencia/{}/{}/{}'.format(
        etapa,
        st,
        user.id))

    with pytest.raises(AttributeError) as exception:
        diligencia_documental(request, etapa, st, user.id)

    # __import__('ipdb').set_trace()
    assert 'AttributeError' == exception.typename
