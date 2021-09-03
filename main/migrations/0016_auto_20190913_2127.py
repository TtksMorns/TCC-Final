# Generated by Django 2.2.4 on 2019-09-14 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190913_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almossom',
            name='bandas',
            field=models.ManyToManyField(through='main.ProgramacaoAlmossom', to='main.Banda'),
        ),
        migrations.AlterField(
            model_name='programacaoalmossom',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Banda'),
        ),
    ]
