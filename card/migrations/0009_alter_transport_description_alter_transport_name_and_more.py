# Generated by Django 4.2.11 on 2024-06-13 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_card_contact_bride_name_1_card_contact_bride_name_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=10, null=True)),
                ('bank', models.CharField(blank=True, max_length=10, null=True)),
                ('number', models.CharField(blank=True, max_length=30, null=True)),
                ('holder', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='card.card')),
            ],
        ),
    ]
