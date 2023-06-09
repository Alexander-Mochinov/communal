# Generated by Django 3.2.13 on 2023-03-21 22:41

from django.db import migrations, models
import django.db.models.deletion
import users.models.users


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230319_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=100, null=True, verbose_name='Дом')),
                ('frame', models.CharField(blank=True, max_length=100, null=True, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Корпус')),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.users.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address'),
        ),
    ]
