
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from app.models import *
from app.forms import (
    UsuarioForm,
    FilmeForm,
    SerieForm,
    AvaliacaoForm,
    CategoriaForm,
    RelatorioForm,
)

from django.views import View
from .models import Filme, Serie, Avaliacao, Categoria, Relatorio,Usuario

# Remova ou comente esta linha
# from app.views import IndexView  # ou qualquer outra view que você tenha
def index(request):
    filmes = Filme.objects.all()  # Ajuste a query conforme necessário
    return render(request, 'index.html', {'filmes': filmes})


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        # Exemplo de processamento de dados do formulário
        data = request.POST.get('field_name')
        if data:
            # Realize alguma ação com os dados recebidos
            # Por exemplo, salvar em um banco de dados ou realizar cálculos
            return redirect('success_url')  # Redireciona após o processamento
        # Se não houver dados, retorne uma resposta ou renderize novamente
        return render(request, 'index.html', {'error': 'Campo obrigatório.'})
        
# VIEWS USUARIO
class UsuarioListView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario_list.html', {'usuarios': usuarios})

class UsuarioCreateView(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'usuario_form.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
        return render(request, 'usuario_form.html', {'form': form})

class UsuarioUpdateView(View):
    def get(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        form = UsuarioForm(instance=usuario)
        return render(request, 'usuario_form.html', {'form': form})

    def post(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
        return render(request, 'usuario_form.html', {'form': form})

class UsuarioDeleteView(View):
    def post(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return redirect('usuario_list')

# VIEWS FILME
class FilmeListView(View):
    def get(self, request):
        filmes = Filme.objects.all()
        return render(request, 'filme_list.html', {'filmes': filmes})

class FilmeCreateView(View):
    def get(self, request):
        form = FilmeForm()
        return render(request, 'filme_form.html', {'form': form})

    def post(self, request):
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
        return render(request, 'filme_form.html', {'form': form})

class FilmeUpdateView(View):
    def get(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(instance=filme)
        return render(request, 'filme_form.html', {'form': form})

    def post(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('filme_list')
        return render(request, 'filme_form.html', {'form': form})

class FilmeDeleteView(View):
    def post(self, request, pk):
        filme = Filme.objects.get(pk=pk)
        filme.delete()
        return redirect('filme_list')

# VIEWS SERIE

class SerieListView(View):
    def get(self, request):
        series = Serie.objects.all()
        return render(request, 'serie_list.html', {'series': series})

class SerieCreateView(View):
    def get(self, request):
        form = SerieForm()
        return render(request, 'serie_form.html', {'form': form})

    def post(self, request):
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
        return render(request, 'serie_form.html', {'form': form})

class SerieUpdateView(View):
    def get(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(instance=serie)
        return render(request, 'serie_form.html', {'form': form})

    def post(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('serie_list')
        return render(request, 'serie_form.html', {'form': form})

class SerieDeleteView(View):
    def post(self, request, pk):
        serie = Serie.objects.get(pk=pk)
        serie.delete()
        return redirect('serie_list')
    



# VIEWS AVALIACAO
class AvaliacaoListView(View):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao_list.html', {'avaliacoes': avaliacoes})

class AvaliacaoCreateView(View):
    def get(self, request):
        form = AvaliacaoForm()
        return render(request, 'avaliacao_form.html', {'form': form})

    def post(self, request):
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
        return render(request, 'avaliacao_form.html', {'form': form})

class AvaliacaoUpdateView(View):
    def get(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(instance=avaliacao)
        return render(request, 'avaliacao_form.html', {'form': form})

    def post(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
        return render(request, 'avaliacao_form.html', {'form': form})

class AvaliacaoDeleteView(View):
    def post(self, request, pk):
        avaliacao = Avaliacao.objects.get(pk=pk)
        avaliacao.delete()
        return redirect('avaliacao_list')

# VIEWS CATEGORIA
class CategoriaListView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'categoria_list.html', {'categorias': categorias})

class CategoriaCreateView(View):
    def get(self, request):
        form = CategoriaForm()
        return render(request, 'categoria_form.html', {'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categoria_form.html', {'form': form})

class CategoriaUpdateView(View):
    def get(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(instance=categoria)
        return render(request, 'categoria_form.html', {'form': form})

    def post(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categoria_form.html', {'form': form})

class CategoriaDeleteView(View):
    def post(self, request, pk):
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return redirect('categoria_list')

# VIEWS RELATORIO
class RelatorioListView(View):
    def get(self, request):
        relatorios = Relatorio.objects.all()
        return render(request, 'relatorio_list.html', {'relatorios': relatorios})

class RelatorioCreateView(View):
    def get(self, request):
        form = RelatorioForm()
        return render(request, 'relatorio_form.html', {'form': form})

    def post(self, request):
        form = RelatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorio_list')
        return render(request, 'relatorio_form.html', {'form': form})

class RelatorioUpdateView(View):
    def get(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(instance=relatorio)
        return render(request, 'relatorio_form.html', {'form': form})

    def post(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            return redirect('relatorio_list')
        return render(request, 'relatorio_form.html', {'form': form})

class RelatorioDeleteView(View):
    def post(self, request, pk):
        relatorio = Relatorio.objects.get(pk=pk)
        relatorio.delete()
        return redirect('relatorio_list')
