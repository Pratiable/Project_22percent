# Generated by Django 3.2.5 on 2021-07-28 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deals', '0001_initial'),
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'banks',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('kakao_id', models.IntegerField(null=True, unique=True)),
                ('deposit_amount', models.IntegerField(default=0)),
                ('deposit_account', models.CharField(max_length=50, unique=True)),
                ('withdrawal_account', models.CharField(max_length=50, null=True, unique=True)),
                ('net_invest_limit', models.IntegerField(default=30000000)),
                ('net_mortgage_invest_limit', models.IntegerField(default=10000000)),
                ('credit_invest_limit', models.IntegerField(default=1000000)),
                ('mortgage_invest_limit', models.IntegerField(default=5000000)),
                ('is_activate', models.BooleanField(default=True)),
                ('deal', models.ManyToManyField(through='investments.UserDeal', to='deals.Deal')),
                ('deposit_bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deposit_bank', to='users.bank')),
                ('withdrawal_bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='withdrawal_bank', to='users.bank')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
