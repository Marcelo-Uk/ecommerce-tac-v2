# Generated by Django 5.1.3 on 2024-11-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendente'), ('PAID', 'Pago'), ('FAILED', 'Falhou')], default='PENDING', max_length=10),
        ),
    ]
