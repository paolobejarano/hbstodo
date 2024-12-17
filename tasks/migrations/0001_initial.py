# Generated by Django 5.1.4 on 2024-12-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('state', models.CharField(choices=[('COMPLETED', 'Completed'), ('IN_PROGRESS', 'In Progress'), ('PENDING', 'Pending')], default='PENDING', max_length=15)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]