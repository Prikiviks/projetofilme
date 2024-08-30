from django.contrib import admin
from django.urls import path
from django.urls import path, include
from app.views import (
    IndexView,
    UsuarioListView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    FilmeListView,
    FilmeCreateView,
    FilmeUpdateView,
    FilmeDeleteView,
    SerieListView,
    SerieCreateView,
    SerieUpdateView,
    SerieDeleteView,
    AvaliacaoListView,
    AvaliacaoCreateView,
    AvaliacaoUpdateView,
    AvaliacaoDeleteView,
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    RelatorioListView,
    RelatorioCreateView,
    RelatorioUpdateView,
    RelatorioDeleteView,
)

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    # URLs para Usuários
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/novo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/deletar/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    # URLs para Filmes
    path('filmes/', FilmeListView.as_view(), name='filme_list'),
    path('filmes/novo/', FilmeCreateView.as_view(), name='filme_create'),
    path('filmes/<int:pk>/editar/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filmes/<int:pk>/deletar/', FilmeDeleteView.as_view(), name='filme_delete'),

    # URLs para Séries
    path('series/', SerieListView.as_view(), name='serie_list'),
    path('series/novo/', SerieCreateView.as_view(), name='serie_create'),
    path('series/<int:pk>/editar/', SerieUpdateView.as_view(), name='serie_update'),
    path('series/<int:pk>/deletar/', SerieDeleteView.as_view(), name='serie_delete'),

    # URLs para Avaliações
    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacao_list'),
    path('avaliacoes/novo/', AvaliacaoCreateView.as_view(), name='avaliacao_create'),
    path('avaliacoes/<int:pk>/editar/', AvaliacaoUpdateView.as_view(), name='avaliacao_update'),
    path('avaliacoes/<int:pk>/deletar/', AvaliacaoDeleteView.as_view(), name='avaliacao_delete'),

    # URLs para Categorias
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/deletar/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    # URLs para Relatórios
    path('relatorios/', RelatorioListView.as_view(), name='relatorio_list'),
    path('relatorios/novo/', RelatorioCreateView.as_view(), name='relatorio_create'),
    path('relatorios/<int:pk>/editar/', RelatorioUpdateView.as_view(), name='relatorio_update'),
    path('relatorios/<int:pk>/deletar/', RelatorioDeleteView.as_view(), name='relatorio_delete'),
]
