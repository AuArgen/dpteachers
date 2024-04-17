# Generated by Django 5.0.4 on 2024-04-17 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klass', '0003_alter_klass_options'),
        ('klassteacher', '0001_initial'),
        ('teacher', '0003_alter_teacher_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasssteacher',
            name='klass',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='klass.klass', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='klasssteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Мугалим'),
        ),
    ]
