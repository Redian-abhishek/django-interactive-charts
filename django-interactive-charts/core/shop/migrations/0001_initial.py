# Generated by Django 4.2 on 2024-05-10 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_full_name', models.CharField(max_length=64)),
                ('payment_method', models.CharField(choices=[('CC', 'Credit card'), ('DC', 'Debit card'), ('ET', 'Ethereum'), ('BC', 'Bitcoin')], default='CC', max_length=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('successful', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
