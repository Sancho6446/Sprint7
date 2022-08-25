# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.TextField()
    new_type = models.TextField()
    user_action = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'Auditoria_Cuenta'


class Marcatarjeta(models.Model):
    marcaid = models.AutoField(db_column='MarcaId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'MarcaTarjeta'


class Movimientos(models.Model):
    mov_id = models.AutoField(primary_key=True)
    nro_cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='nro_cuenta')
    monto = models.IntegerField()
    op_type = models.TextField()
    hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'Movimientos'


class Tipocuenta(models.Model):
    tipocuentaid = models.AutoField(db_column='tipoCuentaId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'TipoCuenta'


class Tiposclientes(models.Model):
    tipoid = models.AutoField(db_column='TipoId', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'TiposClientes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipocuentaid = models.ForeignKey(Tipocuenta, models.DO_NOTHING, db_column='tipoCuentaId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direcciones(models.Model):
    calle = models.TextField(primary_key=True)
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)
    branch = models.OneToOneField('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numerotarjeta = models.AutoField(db_column='NumeroTarjeta', primary_key=True)  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    fecha_de_otorgamiento = models.DateField()
    fecha_de_expiracion = models.DateField()
    tipo_tarjeta = models.TextField()
    marcaid = models.ForeignKey(Marcatarjeta, models.DO_NOTHING, db_column='marcaId')  # Field name made lowercase.
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'