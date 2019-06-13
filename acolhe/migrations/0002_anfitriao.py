# Generated by Django 2.2.2 on 2019-06-13 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acolhe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anfitriao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('contato', models.CharField(max_length=11)),
                ('descricao', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anfitriao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
