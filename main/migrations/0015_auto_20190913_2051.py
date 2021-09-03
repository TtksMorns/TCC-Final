# Generated by Django 2.2.4 on 2019-09-13 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190911_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='almossom',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/almosom_pics'),
        ),
        migrations.AddField(
            model_name='almossom',
            name='info',
            field=models.CharField(max_length=100, null=True),
        ),
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