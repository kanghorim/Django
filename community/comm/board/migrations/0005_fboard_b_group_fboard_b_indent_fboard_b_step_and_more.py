# Generated by Django 4.0.2 on 2022-02-10 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_fboard_b_img_alter_fboard_b_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fboard',
            name='b_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fboard',
            name='b_indent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fboard',
            name='b_step',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 10, 14, 43, 41, 123236)),
        ),
        migrations.AlterField(
            model_name='fboard',
            name='b_no',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
