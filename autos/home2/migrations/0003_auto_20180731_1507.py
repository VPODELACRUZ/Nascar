# Generated by Django 2.0.6 on 2018-07-31 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0002_carrera_competidores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piloto',
            name='patrocinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home2.Patrocinador'),
        ),
    ]
