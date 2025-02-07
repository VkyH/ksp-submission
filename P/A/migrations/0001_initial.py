# Generated by Django 4.1.5 on 2023-02-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('District_Name', models.CharField(choices=[('Bagalkot', 'Bagalkot'), ('Ballari', 'Ballari'), ('Belagavi', 'Belagavi'), ('Bengaluru Rural', 'Bengaluru Rural'), ('Bengaluru Urban', 'Bengaluru Urban'), ('Bidar', 'Bidar'), ('Chamarajanagar', 'Chamarajanagar'), ('Chikkaballapura', 'Chikkaballapura'), ('Chikkamagaluru', 'Chikkamagaluru'), ('Chitradurga', 'Chitradurga'), ('Dakshina Kannada', 'Dakshina Kannada'), ('Davangere', 'Davangere'), ('Dharwad', 'Dharwad'), ('Gadag', 'Gadag'), ('Gulbarga', 'Gulbarga'), ('Hassan', 'Hassan'), ('Haveri', 'Haveri'), ('Kalaburagi', 'Kalaburagi'), ('Kodagu', 'Kodagu'), ('Kolar', 'Kolar'), ('Koppal', 'Koppal'), ('Mandya', 'Mandya'), ('Mysuru', 'Mysuru'), ('Raichur', 'Raichur'), ('Ramanagara', 'Ramanagara'), ('Shivamogga', 'Shivamogga'), ('Tumakuru', 'Tumakuru'), ('Udupi', 'Udupi'), ('Uttara Kannada', 'Uttara Kannada'), ('Vijayapura', 'Vijayapura'), ('Yadgir', 'Yadgir')], max_length=50)),
                ('UnitName', models.CharField(max_length=100)),
                ('FIRNo', models.CharField(max_length=15)),
                ('FIR_Date', models.DateTimeField(auto_now_add=True)),
                ('FIR_Stage', models.BooleanField(default=False)),
                ('Photo_Full_front', models.CharField(max_length=500)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('Person_Name', models.CharField(max_length=200)),
                ('age', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
