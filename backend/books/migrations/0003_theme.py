# Generated by Django 4.2.17 on 2024-12-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_author_alter_book_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(default='#3498db', max_length=7)),
                ('secondary_color', models.CharField(default='#2ecc71', max_length=7)),
                ('accent_color', models.CharField(default='#e74c3c', max_length=7)),
            ],
        ),
    ]
