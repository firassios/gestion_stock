# Generated by Django 3.1.5 on 2021-02-15 13:38

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250, null=True)),
                ('prix', models.DecimalField(decimal_places=3, default=0.0, max_digits=20)),
                ('image', models.ImageField(blank=True, default='products/default.png', upload_to=product.models.upload_to, verbose_name='Image')),
                ('quantite', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-quantite',),
            },
        ),
    ]
