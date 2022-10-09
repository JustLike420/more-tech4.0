# Generated by Django 4.1.2 on 2022-10-08 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_account_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.CharField(choices=[('admin', 'admin'), ('employee', 'employee'), ('editor', 'editor')], max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='main.wallet'),
        ),
    ]
