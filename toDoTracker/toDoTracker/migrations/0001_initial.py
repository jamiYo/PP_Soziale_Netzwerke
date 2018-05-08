# Generated by Django 2.0.5 on 2018-05-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toDo_text', models.CharField(max_length=160)),
                ('due_date', models.DateTimeField()),
                ('progress', models.IntegerField(default=0)),
            ],
        ),
    ]
