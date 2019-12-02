# Generated by Django 2.2.7 on 2019-12-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_record_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='event_type',
            field=models.CharField(choices=[('active', 'active'), ('old', 'old')], default='active', max_length=2),
            preserve_default=False,
        ),
    ]
