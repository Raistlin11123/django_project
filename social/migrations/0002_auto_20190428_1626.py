# Generated by Django 2.2 on 2019-04-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentpost',
            name='id_profil',
        ),
        migrations.RemoveField(
            model_name='commentpost',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='social.CommentPost'),
        ),
    ]
