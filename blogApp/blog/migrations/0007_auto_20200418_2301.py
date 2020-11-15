# Generated by Django 2.2 on 2020-04-19 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200418_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]