# Generated by Django 2.2.19 on 2024-04-23 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Валюта')),
                ('slug', models.SlugField(max_length=3, unique=True, verbose_name='Код')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип валюты')),
                ('slug', models.SlugField(max_length=10, unique=True, verbose_name='Код')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тип платежа')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Код')),
                ('code', models.CharField(max_length=6, verbose_name='Наименование')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Пользователь')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Имя')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(default=0)),
                ('FactOrPlanned', models.BooleanField(default=True, verbose_name='Фактический')),
                ('TakeIntoReports', models.BooleanField(default=True, verbose_name='Учитывать в отчетах')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.Currency', verbose_name='Платеж')),
                ('currency_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.CurrencyType', verbose_name='Платеж')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.PaymentType', verbose_name='Платеж')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payments.Person', verbose_name='Платеж')),
            ],
            options={
                'verbose_name': ('Платеж',),
                'verbose_name_plural': ('Платежи',),
                'ordering': ('-payment_date',),
            },
        ),
    ]
