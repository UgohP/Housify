# Generated by Django 5.0.6 on 2024-05-23 09:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.BigIntegerField(null=True)),
                ('is_vendor', models.BooleanField(blank=True, default=False, null=True)),
                ('in_process', models.BooleanField(blank=True, default=False, null=True)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(blank=True, default='What is your username', max_length=255)),
                ('answer1', models.CharField(blank=True, default='', max_length=255)),
                ('question2', models.CharField(blank=True, default='What is your favourite colour?', max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('username', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Kastina', 'Kastina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'), ('FCT (Abuja)', 'FCT (Abuja)')], max_length=100, null=True)),
                ('location', models.TextField(null=True)),
                ('vendor_email', models.EmailField(blank=True, max_length=254)),
                ('vendor_phone_number1', models.BigIntegerField(null=True)),
                ('vendor_phone_number2', models.BigIntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('vendor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Kastina', 'Kastina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'), ('FCT (Abuja)', 'FCT (Abuja)')], max_length=100, null=True)),
                ('location', models.TextField(null=True)),
                ('phone_number1', models.BigIntegerField(null=True)),
                ('phone_number2', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('how_did_you_here_about_us', models.CharField(choices=[('WhatsApp', 'WhatsApp'), ('Instagram', 'Instagram'), ('X or Twitter', 'X or Twitter'), ('Someone', 'Someone'), ('Other', 'Other')], max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('Means_of_Identification', models.CharField(choices=[('NIN', 'NIN'), ("Driver's License", "Driver's License"), ("Voter's Card", "Voter's Card")], max_length=100, null=True)),
                ('front_view', models.ImageField(null=True, upload_to='image/')),
                ('back_view', models.ImageField(null=True, upload_to='image/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]