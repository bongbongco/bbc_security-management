# Generated by Django 2.0.3 on 2018-04-09 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etas', '0024_worker_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='comment',
            field=models.CharField(max_length=80, null=True, verbose_name='상태'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.BooleanField(verbose_name='수행 여부'),
        ),
    ]
