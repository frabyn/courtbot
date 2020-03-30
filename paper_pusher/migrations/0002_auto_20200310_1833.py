# Generated by Django 3.0.4 on 2020-03-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_pusher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courtform',
            name='form_number',
            field=models.CharField(blank=True, max_length=3, verbose_name='CCL Form Number'),
        ),
        migrations.AddField(
            model_name='courtform',
            name='name',
            field=models.CharField(default='form', max_length=40, verbose_name='Form'),
            preserve_default=False,
        ),
    ]
