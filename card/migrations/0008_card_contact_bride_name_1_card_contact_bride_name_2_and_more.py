# Generated by Django 4.2.11 on 2024-06-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_transport_created_at_transport_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='contact_bride_name_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_name_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_name_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_phone_number_1',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_phone_number_2',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_phone_number_3',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_title_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_title_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_bride_title_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_name_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_name_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_name_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_phone_number_1',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_phone_number_2',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_phone_number_3',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_title_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_title_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='contact_groom_title_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
