# Generated by Django 2.1 on 2018-08-16 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='reward.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_company_name', models.CharField(max_length=100)),
                ('product_img', models.CharField(max_length=200)),
                ('product_detail_img', models.CharField(max_length=200)),
                ('product_interested_count', models.PositiveIntegerField(blank=True, default=0)),
                ('product_start_time', models.CharField(max_length=100)),
                ('product_end_time', models.CharField(max_length=100)),
                ('product_is_funding', models.CharField(choices=[('YA', 'Yes'), ('NA', 'No')], default='YA', max_length=3)),
                ('product_video_url', models.CharField(max_length=100)),
                ('product_cur_amount', models.PositiveIntegerField(blank=True, default=0)),
                ('product_total_amount', models.PositiveIntegerField(default=0)),
                ('product_description', models.TextField(blank=True)),
                ('product_like_user', models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_name', models.CharField(max_length=200)),
                ('reward_option', models.TextField()),
                ('reward_price', models.PositiveIntegerField(default=0)),
                ('reward_shipping_charge', models.PositiveIntegerField(default=0)),
                ('reward_expecting_departure_date', models.CharField(max_length=100)),
                ('reward_total_count', models.PositiveIntegerField(default=0)),
                ('reward_sold_count', models.PositiveIntegerField(default=0)),
                ('reward_on_sale', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='reward.Product')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reward.Reward'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
