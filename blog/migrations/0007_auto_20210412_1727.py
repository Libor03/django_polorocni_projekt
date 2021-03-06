# Generated by Django 3.1.2 on 2021-04-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210412_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name of animal'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='media/animal/%Y/%m/%d/', verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.ManyToManyField(help_text='Select a type for this animal', to='blog.Type'),
        ),
    ]
