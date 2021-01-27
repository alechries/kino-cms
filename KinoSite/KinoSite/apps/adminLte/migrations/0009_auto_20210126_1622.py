# Generated by Django 3.1.5 on 2021-01-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLte', '0008_merge_20210126_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemahall',
            name='cinema_scheme',
            field=models.ImageField(default=0, upload_to='images/hall/logo/', verbose_name='Схема зала'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='news_status',
            field=models.CharField(choices=[('ON', 'Active'), ('OFF', 'Inactive')], max_length=3, verbose_name='Выбор статуса'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promo_status',
            field=models.CharField(choices=[('ON', 'Active'), ('OFF', 'Inactive')], max_length=3, verbose_name='Выбор статуса'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promo_url',
            field=models.URLField(null=True, verbose_name='Ссылка на акцию'),
        ),
    ]