# Generated by Django 4.2.6 on 2023-10-05 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.storage')),
                ('technic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.technic')),
            ],
            options={
                'verbose_name': 'Количество единиц техники',
                'verbose_name_plural': 'Количество единиц техники',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.employee')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.storage')),
                ('technic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.technic')),
            ],
            options={
                'verbose_name': 'Приход',
                'verbose_name_plural': 'Приходы',
            },
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.employee')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.storage')),
                ('technic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='storages.technic')),
            ],
            options={
                'verbose_name': 'Отпуск',
                'verbose_name_plural': 'Отпуски',
            },
        ),
    ]
