# Generated by Django 4.1.7 on 2023-03-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default='+880', max_length=10, null=True),
        ),
    ]
