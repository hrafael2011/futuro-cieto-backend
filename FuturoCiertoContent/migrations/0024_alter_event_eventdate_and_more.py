# Generated by Django 5.1.1 on 2024-10-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturoCiertoContent', '0023_event_textalt_historicalevent_textalt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historicalevent',
            name='EventDate',
            field=models.DateTimeField(),
        ),
    ]
