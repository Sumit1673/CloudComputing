# Generated by Django 2.2.16 on 2020-11-07 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201103_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitaldatamodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='hospitaldatamodel',
            name='country',
        ),
        migrations.AddField(
            model_name='staffdatamodel',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffdatamodel',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.HospitalDataModel'),
        ),
    ]
