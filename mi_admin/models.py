# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Configuracion(models.Model):
    id_config = models.IntegerField(primary_key=True)
    server_ip = models.CharField(max_length=45)
    pic_max = models.IntegerField()
    pic_min = models.IntegerField()
    dev_pic_path = models.CharField(max_length=135)
    pic_server_ip = models.CharField(max_length=45)
    pic_server_path = models.CharField(max_length=135)
    pic_server_user = models.CharField(max_length=60)
    pic_server_pw = models.CharField(max_length=60)
    reg_server_ip = models.CharField(max_length=45)
    rep_server_port = models.IntegerField()
    reg_server_dalay = models.IntegerField()
    purge_interval = models.IntegerField()
    pw_reset_interval = models.IntegerField()
    class Meta:
        db_table = u'configuracion'
        verbose_name_plural='Configuraciones'        
    def __unicode__(self):
        return "Config "+str(self.id_config)
class Dispositivo(models.Model):
    genereted_id = models.CharField(max_length=150, primary_key=True)
    asigned_id = models.IntegerField(unique=True)
    id_config = models.ForeignKey(Configuracion, db_column='id_config')
    class Meta:
        db_table = u'dispositivo'

class Usuario(models.Model):
    username = models.CharField(max_length=60, primary_key=True)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    device = models.ForeignKey(Dispositivo, null=True, blank=True)
    class Meta:
        db_table = u'usuario'
    def __unicode__(self):
        return self.name+" "+self.last_name