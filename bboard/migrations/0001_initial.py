# Generated by Django 2.2.4 on 2019-08-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
