# Generated by Django 3.2.13 on 2023-03-22 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_auto_20230321_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='answer',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('under_consideration', 'На рассмотрении'), ('processed', 'Обработано'), ('closed', 'Закрыта')], default='PROCESSED', max_length=100, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='appeal',
            field=models.TextField(verbose_name='Обращение'),
        ),
    ]
