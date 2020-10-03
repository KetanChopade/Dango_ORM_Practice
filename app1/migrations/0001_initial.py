# Generated by Django 3.0.8 on 2020-10-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]