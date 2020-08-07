# Generated by Django 3.1 on 2020-08-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200807_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='postspage',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postspage',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postspage',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
    ]