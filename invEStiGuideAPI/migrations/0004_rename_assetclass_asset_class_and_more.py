# Generated by Django 4.0.5 on 2022-07-01 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invEStiGuideAPI', '0003_alter_fund_image_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssetClass',
            new_name='Asset_Class',
        ),
        migrations.RenameField(
            model_name='asset_class',
            old_name='asset_class',
            new_name='aclass',
        ),
        migrations.RenameField(
            model_name='fund',
            old_name='asset_class',
            new_name='aclass',
        ),
    ]
