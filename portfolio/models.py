from django.db import models


class Area(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=80)
    areas = models.ManyToManyField(Area)

    def __str__(self) -> str:
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=80)
    linkedin = models.TextField(null=True, blank=True)
    portfolio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome


class Artigo(models.Model):
    nome = models.CharField(max_length=80)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.autor.nome}: {self.nome}'


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.CharField(max_length=80)
    texto = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.artigo.nome}: {self.autor}: {self.likes}'


class Cadeira(models.Model):
    nome = models.TextField()


class Projeto(models.Model):
    participantes = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome = models.TextField()
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    ano = models.IntegerField()
    cadeira = models.ForeignKey(Cadeira, null=True, blank=True, on_delete=models.CASCADE)
    git = models.TextField(null=True, blank=True)


class PrevisaoMetereologica(models.Model):
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()

    def __str__(self):
        return f'Temperatura Mínima: {self.temp_min}, Temperatura Máxima: {self.temp_max}'
