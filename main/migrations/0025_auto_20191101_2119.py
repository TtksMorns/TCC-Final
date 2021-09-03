# Generated by Django 2.2.4 on 2019-11-02 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20191101_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almossom',
            name='bandas',
            field=models.ManyToManyField(related_name='bandas', through='main.ProgramacaoAlmossom', to='main.Banda'),
        ),
        migrations.AlterField(
            model_name='programacaoalmossom',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Banda'),
        ),
    ]
