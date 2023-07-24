# Generated by Django 4.2.3 on 2023-07-24 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
            },
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
        migrations.CreateModel(
            name='CharacterStorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.character', verbose_name='characters')),
                ('stories', models.ManyToManyField(to='library.history', verbose_name='histories')),
            ],
            options={
                'verbose_name': 'CharacterStorie',
                'verbose_name_plural': 'CharacterStories',
            },
        ),
    ]
