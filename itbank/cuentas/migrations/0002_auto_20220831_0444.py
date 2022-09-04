
# Generated by Django 4.1 on 2022-08-31 07:07

from django.db import migrations


def mix_cliente_user(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Cliente = apps.get_model('cuentas', 'Cliente')
    User = apps.get_model('auth', 'User')
    for c in Cliente.objects.all():
        username = f"{c.customer_name.lower()}{c.customer_surname.lower()}{str(c.customer_id)}"
        email = f"{username}@itbank.edu.ar"
        password = "1234"
        user = User.objects.create_user(username, email, password)
        user.first_name = c.customer_name
        user.last_name = c.customer_surname
        c.user = user
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(mix_cliente_user)
    ]
