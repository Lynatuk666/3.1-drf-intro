# Generated by Django 5.1.3 on 2024-11-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-created_at'], 'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
