# Generated by Django 4.2.11 on 2024-07-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0011_alter_card_bride_position_alter_card_groom_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='main_img',
            field=models.ImageField(blank=True, default='noimage.jpg', null=True, upload_to='card/main/'),
        ),
        migrations.AlterField(
            model_name='card',
            name='thumb_img',
            field=models.ImageField(blank=True, default='noimage.jpg', null=True, upload_to='card/thumb/'),
        ),
    ]
