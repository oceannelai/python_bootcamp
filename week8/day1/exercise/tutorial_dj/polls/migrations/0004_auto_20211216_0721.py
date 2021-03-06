# Generated by Django 3.2.8 on 2021-12-16 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_post_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 16, 7, 21, 19, 20429)),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='polls.Post')),
            ],
        ),
    ]
