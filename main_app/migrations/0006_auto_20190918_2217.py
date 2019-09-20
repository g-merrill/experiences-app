# Generated by Django 2.2.3 on 2019-09-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190918_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='category',
            field=models.CharField(choices=[('Art', 'Art'), ('Food', 'Food'), ('Sports', 'Sports'), ('Adventure', 'Adventure'), ('Workshop', 'Workshop'), ('Other', 'Other')], default='Food', max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=750),
        ),
    ]