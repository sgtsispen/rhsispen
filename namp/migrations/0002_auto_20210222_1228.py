# Generated by Django 3.1.7 on 2021-02-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histstatusfuncional',
            name='fk_status_funcional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='namp.statusfuncional', verbose_name='Status Funcional'),
        ),
        migrations.AlterField(
            model_name='servidor',
            name='id_matricula',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Matrícula'),
        ),
    ]
