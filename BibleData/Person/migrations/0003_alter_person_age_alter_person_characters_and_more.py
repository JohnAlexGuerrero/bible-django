# Generated by Django 5.1.1 on 2024-10-05 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0002_alter_relationship_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='characters',
            field=models.ManyToManyField(blank=True, null=True, to='Person.characteristic'),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
