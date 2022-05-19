# Generated by Django 4.0.4 on 2022-05-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0011_remove_billmodel_django_ledg_paid_d74dbd_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='billmodel',
            index=models.Index(fields=['terms'], name='django_ledg_terms_752251_idx'),
        ),
        migrations.AddIndex(
            model_name='invoicemodel',
            index=models.Index(fields=['terms'], name='django_ledg_terms_3b6577_idx'),
        ),
    ]