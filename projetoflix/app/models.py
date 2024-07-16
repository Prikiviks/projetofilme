from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  # Criptografada
    data_nascimento = models.DateField()
    endereco = models.TextField()
    plano_assinatura = models.ForeignKey('Plano', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Usuários'
    
    def __str__(self):
        return self.nome

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()
    periodo_teste = models.IntegerField()  # em dias
    
    class Meta:
        verbose_name = 'Planos'
    
    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField()
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    meio_pagamento = models.ForeignKey('MeioPagamento', on_delete=models.CASCADE)  # Corrigido nome do campo
    status = models.CharField(max_length=50)  # Adicionado campo status para representar pago, pendente, etc.

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f'Pagamento de {self.usuario.nome} em {self.data_pagamento}. Valor: R$ {self.valor}'

class MeioPagamento(models.Model):  # Corrigido nome da classe para seguir convenção de nomenclatura
    nome = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Meio de Pagamento'
        verbose_name_plural = 'Meios de Pagamento'

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    genero = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    sinopse = models.TextField()
    elenco = models.TextField()
    duracao = models.IntegerField()  # em minutos
    
    class Meta:
        verbose_name = 'Filmes'
    
    def __str__(self):
        return self.titulo
    
    
class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    genero = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    sinopse = models.TextField()
    elenco = models.TextField()
    temporadas = models.IntegerField()
    episodios = models.IntegerField()
    
    class Meta:
        verbose_name = 'Series'
    
    def __str__(self):
        return self.titulo
    
    




class Avaliacao(models.Model):
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Avaliacaos'
    
    def __str__(self):
        return f'Avaliação de {self.usuario.nome} para {self.filme.titulo}'






class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Categorias'
    
    def __str__(self):
        return self.nome
    
    
    
    
class Relatorio(models.Model):
    tipo = models.CharField(max_length=100)  # estatísticas mensais, financeiro, etc.
    data_geracao = models.DateTimeField()
    conteudo = models.TextField()
    
    class Meta:
        verbose_name = 'Relatorios'
    
    def __str__(self):
        return f'Relatório de {self.tipo} em {self.data_geracao}'







class Dispositivo(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    identificador = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Dispositivos'
    
    def __str__(self):
        return f'{self.tipo} de {self.usuario.nome}'
    
    
    
    
    
    


class IdiomaLegenda(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    filmes = models.ManyToManyField('Filme')
    series = models.ManyToManyField('Serie')
    
    class Meta:
        verbose_name = 'Idiomalegendas'
    
    def __str__(self):
        return f'{self.nome} {self.descricao} {self.filmes} {self.series}'
    
    
    
class RedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    link = models.URLField()
    descricao = models.TextField()
    
    class Meta:
        verbose_name = 'RedeSocials'
    
    def __str__(self):
        return self.nome





class Notificacao(models.Model):
    usuario_destinatario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)  # novo filme, promoção, etc.
    conteudo = models.TextField()
    data_envio = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Notificacaos'
    
    def __str__(self):
        return f'Notificação para {self.usuario_destinatario.nome} em {self.data_envio}'








class Recomendacao(models.Model):
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    descricao = models.TextField()
    data_recomendacao = models.DateTimeField()
    usuario_recomendou = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Recomendacaos'
    
    def __str__(self):
        return f'Recomendação de {self.usuario_recomendou.nome} para {self.filme.titulo}'




