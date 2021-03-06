# Generated by Django 2.0.3 on 2018-04-03 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etas', '0005_vulnerability_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etas.Project')),
                ('project_vuln_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etas.Vulnerability')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
