# Generated by Django 5.0.3 on 2024-04-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('question', models.TextField()),
                ('image', models.URLField(blank=True)),
                ('is_true', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionUsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
            ],
        ),
    ]
