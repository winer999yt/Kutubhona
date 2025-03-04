# Generated by Django 5.1.6 on 2025-02-24 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(max_length=10)),
                ('tugilgan_sana', models.DateField()),
                ('kitob_soni', models.IntegerField()),
                ('tirik', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('guruh', models.CharField(max_length=255)),
                ('kurs', models.IntegerField()),
                ('kitob_soni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=255)),
                ('sahifa', models.IntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.kutubxonachi')),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kitob')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.talaba')),
            ],
        ),
    ]
