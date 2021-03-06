# Generated by Django 2.1.3 on 2018-11-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.AddField(
            model_name='book',
            name='brand',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
