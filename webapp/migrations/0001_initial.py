# Generated by Django 4.2.5 on 2023-12-04 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo_album', models.ImageField(blank=True, upload_to='albums/')),
                ('release_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('terms', models.TextField(blank=True)),
                ('payment', models.PositiveIntegerField(null=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.album')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('started_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pen_name', models.CharField(max_length=50, null=True)),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('phone', models.IntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_picture/')),
                ('group', models.ManyToManyField(related_name='musicians', to='webapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(auto_now=True)),
                ('photo_track', models.ImageField(blank=True, upload_to='tracks_photo/')),
                ('media_file', models.FileField(blank=True, upload_to='tracks_audio/')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.album')),
            ],
        ),
        migrations.CreateModel(
            name='MusicianContractStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Accepted'), ('P', 'Pending'), ('D', 'Denied')], max_length=1)),
                ('contract', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.contract')),
                ('musician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.musician')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.organizer'),
        ),
        migrations.AddField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.musician'),
        ),
    ]