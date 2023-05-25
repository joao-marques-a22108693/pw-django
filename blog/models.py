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
