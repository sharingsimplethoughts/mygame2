# Generated by Django 2.2.6 on 2019-10-24 05:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=70)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user/profile_image')),
                ('gender', models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female')], max_length=15, null=True)),
                ('country_code', models.CharField(blank=True, max_length=5, null=True)),
                ('mobile', models.CharField(max_length=200)),
                ('lat', models.CharField(blank=True, max_length=50, null=True)),
                ('lon', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('social_id', models.CharField(blank=True, max_length=200, null=True)),
                ('login_type', models.CharField(choices=[('1', 'Normal'), ('2', 'Facebook'), ('3', 'Google')], max_length=10)),
                ('device_type', models.CharField(choices=[('1', 'Android'), ('2', 'Ios'), ('3', 'Web')], max_length=10)),
                ('device_token', models.CharField(blank=True, max_length=200, null=True)),
                ('total_points', models.PositiveIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_all_level_completed', models.BooleanField(default=False)),
                ('is_online', models.PositiveIntegerField(default=0)),
                ('is_engaged', models.BooleanField(default=False)),
                ('is_mail_verify', models.BooleanField(default=False)),
                ('is_num_verify', models.BooleanField(default=False)),
                ('is_profile_created', models.BooleanField(default=False)),
                ('is_social_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OTPStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('otp', models.CharField(blank=True, max_length=10, null=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkillLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uskill_skill', to='accounts.SkillLevels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uskill_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlackListedToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('token', 'user')},
            },
        ),
    ]
