# Generated by Django 5.1.1 on 2024-11-08 13:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0039_alter_historicalreflectionbyjose_comment1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalreflectionbyjose',
            name='Reflection',
        ),
        migrations.RemoveField(
            model_name='reflectionbyjose',
            name='Reflection',
        ),
        migrations.AlterField(
            model_name='historicalreflectionbyjose',
            name='Comment1',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 1'),
        ),
        migrations.AlterField(
            model_name='historicalreflectionbyjose',
            name='Comment2',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 2'),
        ),
        migrations.AlterField(
            model_name='historicalreflectionbyjose',
            name='Comment3',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 3'),
        ),
        migrations.AlterField(
            model_name='reflectionbyjose',
            name='Comment1',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 1'),
        ),
        migrations.AlterField(
            model_name='reflectionbyjose',
            name='Comment2',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 2'),
        ),
        migrations.AlterField(
            model_name='reflectionbyjose',
            name='Comment3',
            field=ckeditor.fields.RichTextField(default='', max_length=300, verbose_name='Comentario Donante 3'),
        ),
    ]
