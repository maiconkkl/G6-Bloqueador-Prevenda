# Generated by Django 2.0.5 on 2018-05-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prevenda',
            fields=[
                ('prevenda', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'prevendas',
            },
        ),
    ]
