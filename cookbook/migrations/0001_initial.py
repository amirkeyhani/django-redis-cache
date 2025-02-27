# Generated by Django 4.0.6 on 2022-07-31 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'default_related_name': 'foods',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('unit_of_measure', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.food')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(through='cookbook.Ingredient', to='cookbook.food')),
            ],
            options={
                'default_related_name': 'recipes',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook.recipe'),
        ),
    ]
