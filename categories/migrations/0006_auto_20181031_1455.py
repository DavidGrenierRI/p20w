# Generated by Django 2.1.2 on 2018-10-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_category_category_page_image_offset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='at_a_glance_label',
            field=models.CharField(help_text='Rhode Island ??? at a glance', max_length=30),
        ),
    ]
