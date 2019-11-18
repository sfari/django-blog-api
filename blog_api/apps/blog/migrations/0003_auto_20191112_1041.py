# Generated by Django 2.2 on 2019-11-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191105_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
