# Generated by Django 5.1.1 on 2024-10-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_gunpla_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gunpla',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gunpla',
            name='extensions',
            field=models.CharField(default='No extansions available', max_length=255),
        ),
    ]
