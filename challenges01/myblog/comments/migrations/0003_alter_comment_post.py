# Generated by Django 5.1 on 2024-09-19 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_alter_tag_name_alter_post_category'),
        ('comments', '0002_alter_comment_author_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
