# Generated by Django 2.0.2 on 2018-02-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180215_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sondage',
            name='question_sondage',
        ),
        migrations.AddField(
            model_name='sondage',
            name='question_sondage',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]