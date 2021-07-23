# Generated by Django 3.2.5 on 2021-07-23 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebtorPayback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('principal', models.IntegerField()),
                ('interest', models.IntegerField()),
                ('payback_round', models.IntegerField()),
                ('state', models.IntegerField(choices=[(1, 'to be paid'), (2, 'paid'), (3, 'unpaid')])),
                ('payback_date', models.DateField()),
            ],
            options={
                'db_table': 'debtor_paybacks',
            },
        ),
        migrations.CreateModel(
            name='UserDeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('deal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='deals.deal')),
            ],
            options={
                'db_table': 'users_deals',
            },
        ),
        migrations.CreateModel(
            name='UserPayback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('principal', models.IntegerField()),
                ('interest', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('commission', models.IntegerField()),
                ('payback_round', models.IntegerField()),
                ('state', models.IntegerField(choices=[(1, 'to be paid'), (2, 'paid'), (3, 'unpaid')])),
                ('payback_date', models.DateField()),
                ('users_deals', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investments.userdeal')),
            ],
            options={
                'db_table': 'user_paybacks',
            },
        ),
    ]
