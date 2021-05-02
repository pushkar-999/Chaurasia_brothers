# Generated by Django 3.1.7 on 2021-05-02 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='Not Filled', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=25)),
                ('Discription', models.CharField(blank=True, max_length=225, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Tax_slab', models.CharField(choices=[('0%', '0%'), ('5%', '5%'), ('12%', '12%'), ('18%', '18%'), ('28%', '28%')], default='0%', max_length=12)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='display_app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default='No section assigned', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='upcoming_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand', models.IntegerField()),
                ('Products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='display_app.products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='display_app.section'),
        ),
    ]