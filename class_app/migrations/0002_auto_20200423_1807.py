# Generated by Django 2.1.9 on 2020-04-23 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('schools', models.ManyToManyField(blank=True, to='class_app.School')),
            ],
        ),
        migrations.AddField(
            model_name='circle',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_app.Club'),
        ),
    ]
