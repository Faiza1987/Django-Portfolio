# Generated by Django 2.2.3 on 2019-07-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
