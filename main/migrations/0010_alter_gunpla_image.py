# Generated by Django 5.1.1 on 2024-10-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_gunpla_image_alter_gunpla_extensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunpla',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]