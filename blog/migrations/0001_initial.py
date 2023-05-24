# Generated by Django 4.2.1 on 2023-05-24 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.area')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=80)),
                ('texto', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.artigo')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('areas', models.ManyToManyField(to='blog.area')),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor'),
        ),
    ]
