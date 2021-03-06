# Generated by Django 3.0.4 on 2020-03-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'On loan'), ('a', 'Available')], default='a', help_text='Book availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre', max_length=200),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text="Enter the book's language", max_length=200),
        ),
    ]
