# Generated by Django 2.2.2 on 2019-06-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acolhe', '0002_auto_20190620_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='acolhido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anfitriao', to='acolhe.Acolhido'),
        ),
    ]
