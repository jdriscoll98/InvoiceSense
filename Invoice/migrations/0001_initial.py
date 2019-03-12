# Generated by Django 2.0 on 2019-03-12 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0003_package_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Company.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Company.Client')),
            ],
        ),
        migrations.CreateModel(
            name='PaymnetPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='Invoice.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='Company.Package')),
                ('payment_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='Invoice.PaymnetPeriod')),
            ],
        ),
    ]