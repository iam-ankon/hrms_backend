# Generated by Django 5.1.6 on 2025-02-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
