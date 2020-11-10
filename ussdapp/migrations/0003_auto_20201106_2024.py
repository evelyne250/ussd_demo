# Generated by Django 3.1.2 on 2020-11-06 17:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ussdapp', '0002_auto_20201105_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('To', models.CharField(max_length=30)),
                ('Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BankUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('registered_data', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SessionLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Ussd',
        ),
        migrations.AddField(
            model_name='banktransaction',
            name='From',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussdapp.bankuser'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='bankUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ussdapp.bankuser'),
        ),
    ]