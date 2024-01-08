# Generated by Django 4.0.1 on 2024-01-05 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=250)),
                ('status', models.BooleanField(choices=[('done', 'done')], default='pending')),
                ('marks', models.IntegerField()),
                ('assignment_file', models.FileField(upload_to='docs/')),
                ('assign_students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('assignment_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]