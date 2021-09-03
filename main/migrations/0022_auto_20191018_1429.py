# Generated by Django 2.2.4 on 2019-10-18 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20191018_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/events_pics'),
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