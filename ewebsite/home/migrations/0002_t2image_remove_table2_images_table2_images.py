# Generated by Django 4.2.2 on 2023-07-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='T2Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='table2',
            name='images',
        ),
        migrations.AddField(
            model_name='table2',
            name='images',
            field=models.ManyToManyField(to='home.t2image'),
        ),
    ]
