# Generated by Django 3.1.7 on 2021-03-21 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='fa_icon',
            field=models.CharField(default='', max_length=64, verbose_name='Icono FA'),
        ),
        migrations.AddField(
            model_name='service',
            name='fa_rotate',
            field=models.IntegerField(default=0, verbose_name='Rotar icono FA'),
        ),
        migrations.AlterField(
            model_name='member',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='contents.content', verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='contents.content', verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='contents.content', verbose_name='Contenido'),
        ),
    ]
