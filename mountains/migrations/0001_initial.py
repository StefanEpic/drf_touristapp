# Generated by Django 4.2.2 on 2023-06-22 14:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(max_length=2)),
                ('summer', models.CharField(max_length=2)),
                ('autumn', models.CharField(max_length=2)),
                ('spring', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('other_title', models.CharField(blank=True, max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'new'), ('PEN', 'pending'), ('ACC', 'accepted'), ('REJ', 'rejected')], default='NEW', max_length=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.author')),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.level')),
            ],
        ),
        migrations.CreateModel(
            name='MountainImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='mountain_images/%Y/%m/%d/')),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.mountain')),
            ],
        ),
    ]