# Generated by Django 4.1.7 on 2023-07-10 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='user')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('Address', models.TextField(blank=True, default='null', max_length=200)),
                ('pincode', models.IntegerField(blank=True, default=1)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(default='no', max_length=100)),
                ('how_many', models.IntegerField()),
                ('total', models.IntegerField()),
                ('dateandtime', models.DateTimeField(auto_now=True)),
                ('product_request', models.BooleanField(default=True)),
                ('product_accepted', models.BooleanField(default=False)),
                ('riched', models.BooleanField(default=False)),
                ('taken', models.BooleanField(default=False)),
                ('cancel', models.BooleanField(default=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.upload_product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordercus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]