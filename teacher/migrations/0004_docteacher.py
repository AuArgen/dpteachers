# Generated by Django 5.0.4 on 2024-04-20 15:20

import django.db.models.deletion
import teacher.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(blank=True, null=True, upload_to=teacher.models.generate_unique_filename, verbose_name='Документ')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Кошумча маалымат')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Мугалим тандоо ')),
            ],
            options={
                'verbose_name': 'Кошумча маалымат',
                'verbose_name_plural': 'Маалыматтар',
            },
        ),
    ]
