# Generated by Django 5.1.1 on 2024-10-05 01:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bible', '0001_initial'),
        ('Epoch', '0001_initial'),
        ('Person', '0001_initial'),
        ('Place', '0001_initial'),
        ('Thing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('chapter', models.IntegerField()),
                ('verse', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bible.book')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
            },
        ),
        migrations.CreateModel(
            name='RelationshipCita',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reference.cita')),
                ('commandment', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Thing.commandment')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Epoch.event')),
                ('person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Person.person')),
                ('place', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Place.place')),
                ('thing', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Thing.thing')),
            ],
            options={
                'verbose_name': 'RelationshipCita',
                'verbose_name_plural': 'RelationshipCitas',
            },
        ),
    ]
