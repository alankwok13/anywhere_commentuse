# Generated by Django 2.1.5 on 2019-03-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=512)),
                ('content', models.TextField(max_length=256)),
                ('publish', models.DateTimeField()),
            ],
        ),
    ]
