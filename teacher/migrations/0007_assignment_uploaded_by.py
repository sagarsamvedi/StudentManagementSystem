# Generated by Django 4.0.1 on 2024-01-12 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_password'),
        ('teacher', '0006_alter_assignment_assignment_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher'),
        ),
    ]
