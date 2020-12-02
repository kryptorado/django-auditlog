from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0007_object_pk_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='seen_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.SET_NULL,
                blank=True,
                to=settings.AUTH_USER_MODEL,
                null=True,
                related_name="seen_by",
            ),
        ),
    ]