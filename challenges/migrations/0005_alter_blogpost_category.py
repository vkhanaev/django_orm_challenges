# Generated by Django 4.2.3 on 2024-06-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_alter_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(blank=True, choices=[('TECHNOLOGY', 'Технологии'), ('HEALTH', 'Здоровье'), ('EDUCATION', 'Образование'), ('ENTERTAINMENT', 'Развлечения'), ('TRAVEL', 'Путешествия')], max_length=20, null=True),
        ),
    ]
