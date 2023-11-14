# Generated by Django 4.1.4 on 2023-11-01 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('lecID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('lecName', models.CharField(max_length=50)),
                ('lecPhone', models.CharField(max_length=15)),
                ('lecEmail', models.CharField(max_length=30)),
                ('lecPass', models.CharField(default='null', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Case',
            fields=[
                ('caseCode', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('caseClass', models.CharField(max_length=50)),
                ('offences', models.TextField(max_length=500)),
                ('punishment', models.TextField(max_length=500)),
                ('registerText', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=50)),
                ('studentClass', models.CharField(max_length=50)),
                ('studentEmail', models.CharField(max_length=30)),
                ('studentPhone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UTTK_Member',
            fields=[
                ('uttkID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('uttkName', models.CharField(max_length=50)),
                ('uttkPhone', models.CharField(max_length=15)),
                ('uttkEmail', models.CharField(max_length=30)),
                ('uttkPass', models.CharField(default='null', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinary_Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=50)),
                ('studentClass', models.CharField(max_length=50)),
                ('disciplinaryText', models.TextField(max_length=500)),
                ('disciplinaryDate', models.DateField()),
                ('caseCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UTTK.register_case')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UTTK.student')),
            ],
        ),
    ]
