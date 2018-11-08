# Generated by Django 2.1.2 on 2018-10-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20181030_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='homepage_image',
        ),
        migrations.AlterField(
            model_name='category',
            name='at_a_glance_label',
            field=models.CharField(help_text='Rhode Island ??? at a glance', max_length=20),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_page_image',
            field=models.ImageField(upload_to='category_headers'),
        ),
    ]
