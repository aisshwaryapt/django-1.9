# Generated by Django 3.1 on 2020-08-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_postspage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postspage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
