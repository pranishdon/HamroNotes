# Generated by Django 4.1 on 2023-03-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='category',
        ),
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
