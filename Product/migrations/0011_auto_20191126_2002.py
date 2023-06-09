# Generated by Django 2.2.7 on 2019-11-26 14:32

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_auto_20191126_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_by',
            field=django_currentuser.db.models.fields.CurrentUserField(blank=True, default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
