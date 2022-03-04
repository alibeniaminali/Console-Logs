# Generated by Django 4.0.3 on 2022-03-04 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(default=None, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_to_upload', models.CharField(max_length=500)),
                ('video', models.BooleanField(blank=True, default=False)),
                ('screenshot', models.BooleanField(blank=True, default=False)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='games.game')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
