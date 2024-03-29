# Generated by Django 4.0.1 on 2022-01-14 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_alter_financa_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField()),
                ('extra_income', models.FloatField()),
                ('rent_expenses', models.FloatField()),
                ('market_expenses', models.FloatField()),
                ('extra_expenses', models.FloatField()),
                ('receipt_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
        migrations.DeleteModel(
            name='Financa',
        ),
        migrations.AddField(
            model_name='finance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financas.user'),
        ),
    ]
