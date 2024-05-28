# Generated by Django 4.2.13 on 2024-05-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0002_alter_gpu_vram_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branddetail",
            name="market_ocp",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="gpu",
            name="VRAM_cap",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="gpu",
            name="frequency",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="gpu",
            name="power_dissipation",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="price",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
