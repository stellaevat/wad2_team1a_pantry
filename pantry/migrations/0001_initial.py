# Generated by Django 2.2.26 on 2022-03-21 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pantry.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('tab', models.BooleanField(default=False)),
                ('selectable', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('ingredient_type', models.CharField(choices=[('meats', 'Meat, Seafood & Substitutes'), ('dairy', 'Eggs, Dairy & Substitutes'), ('veg', 'Vegetables & Funghi'), ('pulses', 'Pulses'), ('grains', 'Grains, Seeds & Nuts'), ('carbs', 'Bread, Pasta & Rice'), ('fats', 'Fats & Oils'), ('herbs', 'Herbs, Spices & Seasonings'), ('condiments', 'Condiments & Sauces'), ('fruit', 'Fruit'), ('baking', 'Sweet & Baking'), ('drinks', 'Beverages')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=16)),
                ('plural', models.BooleanField(default=False)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('picture', models.ImageField(blank=True, default='recipe_pictures/banner-default.png', upload_to=pantry.models.FileRenamed('recipe_pictures'))),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('servings', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('advanced', 'Advanced')], max_length=16)),
                ('steps', models.CharField(max_length=2048)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('stars', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='pantry.Category')),
                ('ingredients', models.ManyToManyField(through='pantry.IngredientList', to='pantry.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, default='profile-picture-default.png', upload_to=pantry.models.FileRenamed('profile_pictures'))),
                ('starred', models.ManyToManyField(related_name='users', to='pantry.Recipe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientlist',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredientlist',
            unique_together={('recipe', 'ingredient')},
        ),
    ]
