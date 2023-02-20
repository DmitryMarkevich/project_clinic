# Generated by Django 4.1.4 on 2023-01-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantages',
            options={'ordering': ['id'], 'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'ordering': ['id'], 'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['surname'], 'verbose_name': 'Сотрудника', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'ordering': ['id'], 'verbose_name': 'Информацию', 'verbose_name_plural': 'Информация'},
        ),
        migrations.AlterField(
            model_name='client',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clinic_info.service', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clinic_info.professions', verbose_name='Профессия'),
        ),
    ]
