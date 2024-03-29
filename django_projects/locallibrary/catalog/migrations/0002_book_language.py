# Generated by Django 3.0 on 2019-12-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('bu', 'Burmese'), ('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sp', 'Spanish'), ('th', 'Thai'), ('ka', 'Karen')], default='en', help_text='Language the book is written in', max_length=2),
        ),
    ]
