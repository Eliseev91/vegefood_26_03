# Generated by Django 3.0.4 on 2020-04-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(null=True)),
                ('price_sale', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
