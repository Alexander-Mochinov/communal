# Generated by Django 3.2.13 on 2023-03-28 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20230328_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicators',
            old_name='couter',
            new_name='counter',
        ),
        migrations.AlterField(
            model_name='counter',
            name='name',
            field=models.CharField(choices=[('INDICATORS_HOT_WATER', 'Горячая вода'), ('INDICATORS_COLD_WATER', 'Холодная вода'), ('INDICATORS_LIGHT_DAY', 'Дневной период'), ('INDICATORS_LIGHT_NIGHT', 'Ночной период')], max_length=100, unique=True, verbose_name='Показатель'),
        ),
    ]
