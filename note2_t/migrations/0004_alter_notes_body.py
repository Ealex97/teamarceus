# Generated by Django 4.1.2 on 2022-10-16 16:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note2_t', '0003_alter_notes_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]