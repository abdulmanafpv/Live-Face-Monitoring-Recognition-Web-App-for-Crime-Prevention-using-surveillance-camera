# Generated by Django 4.0.3 on 2022-06-24 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face_biometric_app', '0007_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='detected',
            name='proof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='face_biometric_app.proof'),
        ),
    ]
