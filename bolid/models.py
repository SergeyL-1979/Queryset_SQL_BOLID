# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accesszone(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessZone'


class Acesspoint(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    inkeyid = models.IntegerField(db_column='InKeyID', blank=True, null=True)  # Field name made lowercase.
    induration = models.IntegerField(db_column='InDuration', blank=True, null=True)  # Field name made lowercase.
    incommand = models.IntegerField(db_column='InCommand', blank=True, null=True)  # Field name made lowercase.
    outkeyid = models.IntegerField(db_column='OutKeyID', blank=True, null=True)  # Field name made lowercase.
    outduration = models.IntegerField(db_column='OutDuration', blank=True, null=True)  # Field name made lowercase.
    outcommand = models.IntegerField(db_column='OutCommand', blank=True, null=True)  # Field name made lowercase.
    inkeyid2 = models.IntegerField(db_column='InKeyID2', blank=True, null=True)  # Field name made lowercase.
    induration2 = models.IntegerField(db_column='InDuration2', blank=True, null=True)  # Field name made lowercase.
    incommand2 = models.IntegerField(db_column='InCommand2', blank=True, null=True)  # Field name made lowercase.
    outkeyid2 = models.IntegerField(db_column='OutKeyID2', blank=True, null=True)  # Field name made lowercase.
    outduration2 = models.IntegerField(db_column='OutDuration2', blank=True, null=True)  # Field name made lowercase.
    outcommand2 = models.IntegerField(db_column='OutCommand2', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    indexzone1 = models.IntegerField(db_column='IndexZone1', blank=True, null=True)  # Field name made lowercase.
    indexzone2 = models.IntegerField(db_column='IndexZone2', blank=True, null=True)  # Field name made lowercase.
    indexzone3 = models.IntegerField(db_column='IndexZone3', blank=True, null=True)  # Field name made lowercase.
    indexzone4 = models.IntegerField(db_column='IndexZone4', blank=True, null=True)  # Field name made lowercase.
    worktimezone1 = models.IntegerField(db_column='WorkTimeZone1', blank=True, null=True)  # Field name made lowercase.
    worktimezone2 = models.IntegerField(db_column='WorkTimeZone2', blank=True, null=True)  # Field name made lowercase.
    worktimezone3 = models.IntegerField(db_column='WorkTimeZone3', blank=True, null=True)  # Field name made lowercase.
    worktimezone4 = models.IntegerField(db_column='WorkTimeZone4', blank=True, null=True)  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    weightterminalid = models.IntegerField(db_column='WeightTerminalID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcessPoint'


class Applicationmodifdata(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_parent = models.IntegerField(db_column='ID_Parent', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicationModifData'


class Authorities(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='ProgramID')  # Field name made lowercase.
    programsubitemid = models.IntegerField(db_column='ProgramSubItemID', blank=True, null=True)  # Field name made lowercase.
    abrowse = models.IntegerField(db_column='aBrowse', blank=True, null=True)  # Field name made lowercase.
    ainsert = models.IntegerField(db_column='aInsert', blank=True, null=True)  # Field name made lowercase.
    aedit = models.IntegerField(db_column='aEdit', blank=True, null=True)  # Field name made lowercase.
    adelete = models.IntegerField(db_column='aDelete', blank=True, null=True)  # Field name made lowercase.
    archive = models.IntegerField(db_column='Archive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authorities'


class Bindingcommandscenarios(models.Model):
    id_itemsscenarios = models.OneToOneField('Referenceitemsscenarios', models.DO_NOTHING, db_column='ID_ItemsScenarios', primary_key=True)  # Field name made lowercase.
    id_commandscenarios = models.ForeignKey('Referencecommandscenarios', models.DO_NOTHING, db_column='ID_CommandScenarios')  # Field name made lowercase.
    id_level = models.SmallIntegerField(db_column='ID_Level')  # Field name made lowercase.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.
    def_field = models.BooleanField(db_column='Def')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    devvalue = models.TextField(db_column='DevValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isnumber = models.BooleanField(db_column='isNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingCommandScenarios'
        unique_together = (('id_itemsscenarios', 'id_commandscenarios', 'id_level'), ('id_itemsscenarios', 'id_commandscenarios', 'id_level', 'sort'),)


class Bindingconditionstepscen(models.Model):
#     # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_scendevice = models.ForeignKey('Scenariosdevice', models.DO_NOTHING, db_column='ID_ScenDevice')  # Field name made lowercase.
    access = models.BooleanField(db_column='Access')  # Field name made lowercase.
    id_conditionscen = models.OneToOneField('Conditionstepscenarios', models.DO_NOTHING, db_column='ID_ConditionScen', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingConditionStepScen'
        unique_together = (('id_conditionscen', 'id_scendevice', 'access'),)


class Bindinggrobjectsstepscen(models.Model):
#     # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_scendevice = models.ForeignKey('Scenariosdevice', models.DO_NOTHING, db_column='ID_ScenDevice')  # Field name made lowercase.
    access = models.BooleanField(db_column='Access')  # Field name made lowercase.
    id_grobject = models.OneToOneField('Groupobj', models.DO_NOTHING, db_column='ID_GrObject', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingGrObjectsStepScen'
        unique_together = (('id_grobject', 'id_scendevice', 'access'),)


class Bindingitemsdevscenarios(models.Model):
    id_elementtype = models.IntegerField(db_column='ID_ElementType', primary_key=True)  # Field name made lowercase.
    id_itemsscenarios = models.ForeignKey('Referenceitemsscenarios', models.DO_NOTHING, db_column='ID_ItemsScenarios')  # Field name made lowercase.
    defvalue = models.TextField(db_column='DefValue')  # Field name made lowercase. This field type is a guess.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingItemsDevScenarios'
        unique_together = (('id_elementtype', 'id_itemsscenarios'),)


class Bindingitemsscenarios(models.Model):
    id_scenariostypes = models.OneToOneField('Referencescenariostypes', models.DO_NOTHING, db_column='ID_ScenariosTypes', primary_key=True)  # Field name made lowercase.
    id_itemsscenarios = models.ForeignKey('Referenceitemsscenarios', models.DO_NOTHING, db_column='ID_ItemsScenarios')  # Field name made lowercase.
    id_level = models.SmallIntegerField(db_column='ID_Level')  # Field name made lowercase.
    def_field = models.BooleanField(db_column='Def')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.
    regexp = models.CharField(db_column='RegExp', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sortexp = models.IntegerField(db_column='SortExp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingItemsScenarios'
        unique_together = (('id_scenariostypes', 'id_itemsscenarios', 'id_level'),)


class Bindingobjectsstepscen(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_scendevice = models.ForeignKey('Scenariosdevice', models.DO_NOTHING, db_column='ID_ScenDevice')  # Field name made lowercase.
    access = models.BooleanField(db_column='Access')  # Field name made lowercase.
    id_object = models.OneToOneField('Pobjects', models.DO_NOTHING, db_column='ID_Object', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BindingObjectsStepScen'
        unique_together = (('id_object', 'id_scendevice', 'access'),)


class Cameramatrix(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matrix = models.BinaryField(db_column='Matrix', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    reserv = models.IntegerField(db_column='Reserv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraMatrix'


class Cameras(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    camnumber = models.IntegerField(db_column='CamNumber', blank=True, null=True)  # Field name made lowercase.
    monnumber = models.IntegerField(db_column='MonNumber', blank=True, null=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='GType', blank=True, null=True)  # Field name made lowercase.
    falertrecord = models.IntegerField(db_column='FAlertRecord', blank=True, null=True)  # Field name made lowercase.
    rectimeafteralarm = models.IntegerField(db_column='RecTimeAfterAlarm', blank=True, null=True)  # Field name made lowercase.
    settings = models.BinaryField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.
    ipcamparams = models.CharField(db_column='IPCamParams', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime', blank=True, null=True)  # Field name made lowercase.
    autotakeoff = models.IntegerField(db_column='AutoTakeOff', blank=True, null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', blank=True, null=True)  # Field name made lowercase.
    ipaddr = models.CharField(db_column='IPAddr', max_length=64, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cameras'


class Clientfieldsnames(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientFieldsNames'


class Clientfieldsvalues(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    field = models.ForeignKey(Clientfieldsnames, models.DO_NOTHING)
    owner = models.ForeignKey('Plist', models.DO_NOTHING, db_column='owner')
    value = models.CharField(max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClientFieldsValues'


class Codeslist(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    letter = models.CharField(db_column='Letter', max_length=4, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CodesList'


class CodesT12(models.Model):
    datec = models.DateTimeField(db_column='DateC')  # Field name made lowercase.
    idhozorgan = models.IntegerField(db_column='IDHOZORGAN')  # Field name made lowercase.
    letterid = models.IntegerField(db_column='LetterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Codes_T12'
        unique_together = (('idhozorgan', 'datec', 'letterid'),)


class Comports(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    adaptor = models.IntegerField(db_column='Adaptor')  # Field name made lowercase.
    pradaptor = models.IntegerField(db_column='PrAdaptor')  # Field name made lowercase.
    porttype = models.IntegerField(db_column='PortType')  # Field name made lowercase.
    adaptoraddress = models.CharField(db_column='AdaptorAddress', max_length=32, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    protokoltype = models.IntegerField(db_column='Protokoltype')  # Field name made lowercase.
    typeline = models.IntegerField(db_column='TypeLine', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    baud = models.IntegerField(db_column='Baud', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComPorts'
        unique_together = (('computerid', 'number'),)


class Comptrns(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    senderid = models.IntegerField(db_column='SenderID')  # Field name made lowercase.
    receptorid = models.IntegerField(db_column='ReceptorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompTrns'


class Comps(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='Gindex', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    psevdonim = models.CharField(db_column='Psevdonim', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tcp_ip = models.CharField(db_column='TCP_IP', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    works = models.IntegerField(db_column='Works', blank=True, null=True)  # Field name made lowercase.
    typeevents = models.IntegerField(db_column='TypeEvents', blank=True, null=True)  # Field name made lowercase.
    ipreservsrv = models.CharField(db_column='IpReservSrv', max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    abonentnumber = models.CharField(db_column='AbonentNumber', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    applicationguid = models.CharField(db_column='ApplicationGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comps'


class Conditionstepscenarios(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    latname = models.CharField(db_column='LatName', max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConditionStepScenarios'


class Controlitems(models.Model):
    item_type = models.IntegerField()
    item_id = models.IntegerField()
    tmvl = models.DateTimeField()
    cmd = models.IntegerField()
    action = models.IntegerField()
    guid_cmd = models.CharField(primary_key=True, max_length=64, db_collation='Cyrillic_General_CI_AS')
    id_owner = models.IntegerField(blank=True, null=True)
    result_cmd = models.IntegerField(blank=True, null=True)
    ownercompid = models.IntegerField(db_column='OwnercompId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControlItems'


class Counters(models.Model):
    tablename = models.CharField(db_column='TableName', primary_key=True, max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counters'
        unique_together = (('tablename', 'fieldname'),)


class Devcamerasitems(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    objtype = models.IntegerField(db_column='ObjType')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    camindex = models.IntegerField(db_column='CamIndex')  # Field name made lowercase.
    param = models.IntegerField(db_column='Param', blank=True, null=True)  # Field name made lowercase.
    iseventrec = models.IntegerField(db_column='IsEventRec', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevCamerasItems'


class Develms(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devid = models.IntegerField(db_column='DevID')  # Field name made lowercase.
    gtype = models.IntegerField(db_column='GType')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID')  # Field name made lowercase.
    phonesid = models.IntegerField(db_column='PhonesId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevElms'


class Devitems(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID')  # Field name made lowercase.
    address = models.IntegerField(db_column='Address')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='GType', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='ItemType')  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    command = models.IntegerField(db_column='Command', blank=True, null=True)  # Field name made lowercase.
    timeoutcontrol = models.IntegerField(db_column='TimeOutControl', blank=True, null=True)  # Field name made lowercase.
    timeoutconfig = models.IntegerField(db_column='TimeOutConfig', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevItems'
        unique_together = (('deviceid', 'address', 'itemtype'),)


class Dvsmass(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    icongroup = models.SmallIntegerField(db_column='IconGroup')  # Field name made lowercase.
    groupsort = models.IntegerField(db_column='GroupSort', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.
    left = models.IntegerField(db_column='Left')  # Field name made lowercase.
    top = models.IntegerField(db_column='Top')  # Field name made lowercase.
    width = models.IntegerField(db_column='Width')  # Field name made lowercase.
    height = models.IntegerField(db_column='Height')  # Field name made lowercase.
    largeicon = models.BooleanField(db_column='LargeIcon')  # Field name made lowercase.
    numberrelation = models.IntegerField(db_column='NumberRelation', blank=True, null=True)  # Field name made lowercase.
    resourceico = models.BinaryField(db_column='ResourceIco', blank=True, null=True)  # Field name made lowercase.
    reswidth = models.IntegerField(db_column='ResWidth', blank=True, null=True)  # Field name made lowercase.
    resheight = models.IntegerField(db_column='ResHeight', blank=True, null=True)  # Field name made lowercase.
    rescountico = models.IntegerField(db_column='ResCountIco', blank=True, null=True)  # Field name made lowercase.
    defaultlargeicon = models.BooleanField(db_column='DefaultLargeIcon', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DvsMass'
        unique_together = (('number', 'icongroup', 'largeicon'),)


class Elementstypesgroups(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ElementsTypesGroups'


class Evreply(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    source = models.IntegerField(db_column='Source')  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType')  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID')  # Field name made lowercase.
    scriptid = models.IntegerField(db_column='ScriptID')  # Field name made lowercase.
    data = models.IntegerField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EvReply'


class Eventgroup(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventGroup'


class Eventgroupcont(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventgroupid = models.IntegerField(db_column='EventGroupID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventGroupCont'


class Eventonmodificationdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='ChangeDate',)  # Field name made lowercase.
    id_application = models.ForeignKey(Applicationmodifdata, models.DO_NOTHING, db_column='ID_Application')  # Field name made lowercase.
    updatestatus = models.IntegerField(db_column='UpdateStatus')  # Field name made lowercase.
    aguid = models.CharField(db_column='AGuid', max_length=500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_subj = models.IntegerField(db_column='ID_Subj', blank=True, null=True)  # Field name made lowercase.
    subj = models.CharField(db_column='Subj', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adata = models.TextField(db_column='AData', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EventOnModificationData'
        unique_together = (('changedate', 'id'),)


class Events(models.Model):
    event = models.IntegerField(db_column='Event', primary_key=True)  # Field name made lowercase.
    charid = models.CharField(db_column='CharID', max_length=2, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='Contents', max_length=60, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    realevent = models.IntegerField(db_column='RealEvent', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    formatview = models.IntegerField(db_column='FormatView', blank=True, null=True)  # Field name made lowercase.
    soundnumber = models.IntegerField(db_column='SoundNumber', blank=True, null=True)  # Field name made lowercase.
    alarmlevel = models.IntegerField(db_column='AlarmLevel', blank=True, null=True)  # Field name made lowercase.
    gpevent = models.IntegerField(db_column='GpEvent', blank=True, null=True)  # Field name made lowercase.
    eventscategoryid = models.IntegerField(db_column='EventsCategoryID', blank=True, null=True)  # Field name made lowercase.
    isalarm = models.IntegerField(db_column='IsAlarm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'

    def __str__(self):
        return '{} {}'.format(self.event, self.contents)


class Eventscategories(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hexcolor = models.CharField(db_column='HexColor', max_length=7, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsCategories'


class Gtime(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calendar = models.BinaryField(db_column='Calendar', blank=True, null=True)  # Field name made lowercase.
    timewintype = models.IntegerField(db_column='TimeWinType', blank=True, null=True)  # Field name made lowercase.
    workmode = models.IntegerField(db_column='WorkMode', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GTime'


class Graccess(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode')  # Field name made lowercase.
    accessid = models.IntegerField(db_column='AccessID')  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    timezone = models.IntegerField(db_column='TimeZone')  # Field name made lowercase.
    antipassback = models.IntegerField(db_column='Antipassback', blank=True, null=True)  # Field name made lowercase.
    pardontime = models.DateTimeField(db_column='PardonTime', blank=True, null=True)  # Field name made lowercase.
    confirmid = models.IntegerField(db_column='ConfirmID', blank=True, null=True)  # Field name made lowercase.
    confirmid2 = models.IntegerField(db_column='ConfirmID2', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    codetype = models.IntegerField(db_column='CodeType', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    config2 = models.IntegerField(db_column='Config2', blank=True, null=True)  # Field name made lowercase.
    pswaddcode = models.IntegerField(db_column='PswAddCode', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrAccess'


class Grobjcont(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    grobjid = models.IntegerField(db_column='GrObjID')  # Field name made lowercase.
    objid = models.IntegerField(db_column='ObjID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrObjCont'
        unique_together = (('grobjid', 'objid'),)


class Groupobj(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    alarmkey = models.IntegerField(db_column='AlarmKey', blank=True, null=True)  # Field name made lowercase.
    guardkey = models.IntegerField(db_column='GuardKey', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupObj'
        unique_together = (('computerid', 'gindex'),)


class Groups(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    istemplate = models.IntegerField(db_column='isTemplate', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    flags2 = models.IntegerField(db_column='Flags2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'


class Gsmsettings(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rslinesid = models.IntegerField(db_column='RsLinesID')  # Field name made lowercase.
    apn = models.CharField(db_column='Apn', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    passw = models.CharField(db_column='Passw', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    smtpserver = models.CharField(db_column='SmtpServer', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    smtpport = models.IntegerField(db_column='SmtpPort', blank=True, null=True)  # Field name made lowercase.
    smtplogin = models.CharField(db_column='SmtpLogin', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    smtppassw = models.CharField(db_column='SmtpPassw', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    smtpmailfrom = models.CharField(db_column='SmtpMailFrom', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    popserver = models.CharField(db_column='PopServer', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    popport = models.IntegerField(db_column='PopPort', blank=True, null=True)  # Field name made lowercase.
    poplogin = models.CharField(db_column='PopLogin', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    poppassw = models.CharField(db_column='PopPassw', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GsmSettings'
        unique_together = (('id', 'rslinesid'),)


class Guest(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    plistid = models.OneToOneField('Plist', models.DO_NOTHING, db_column='PListID')  # Field name made lowercase.
    receivelistid = models.IntegerField(db_column='ReceiveListId', blank=True, null=True)  # Field name made lowercase.
    companyreceive = models.IntegerField(db_column='CompanyReceive', blank=True, null=True)  # Field name made lowercase.
    sectionreceive = models.IntegerField(db_column='SectionReceive', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=240, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    avto = models.CharField(db_column='Avto', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autonumber = models.CharField(db_column='AutoNumber', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    automarka = models.CharField(db_column='Automarka', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autocolor = models.CharField(db_column='AutoColor', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autonigth = models.IntegerField(db_column='AutoNigth', blank=True, null=True)  # Field name made lowercase.
    datevisit = models.DateTimeField(db_column='DateVisit', blank=True, null=True)  # Field name made lowercase.
    receiveguestname = models.CharField(db_column='ReceiveGuestName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receiveguestfamaly = models.CharField(db_column='ReceiveGuestFamaly', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receiveguestsecondname = models.CharField(db_column='ReceiveGuestSecondName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receiveguestroom = models.CharField(db_column='ReceiveGuestRoom', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    receiveguestphone = models.CharField(db_column='ReceiveGuestPhone', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goalvisit = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    ruleaccess = models.IntegerField(db_column='RuleAccess', blank=True, null=True)  # Field name made lowercase.
    idnoface = models.IntegerField(db_column='IDNoFace', blank=True, null=True)  # Field name made lowercase.
    datevisitend = models.DateTimeField(db_column='DateVisitEnd', blank=True, null=True)  # Field name made lowercase.
    recroomid = models.IntegerField(db_column='RecRoomID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Guest'


class Holidays(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    gdate = models.DateTimeField(db_column='GDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Holidays'


class Itemevents(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemevent = models.IntegerField(db_column='ItemEvent')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemEvents'


class Keyobjs(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID')  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KeyObjs'
        unique_together = (('objectid', 'keyid', 'status'),)


class KoneAllaccessmask(models.Model):
    id = models.OneToOneField('KoneDopglobaldefaultaccessmask', models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    floor = models.SmallIntegerField(db_column='Floor')  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF')  # Field name made lowercase.
    sr = models.SmallIntegerField(db_column='SR')  # Field name made lowercase.
    df = models.SmallIntegerField(db_column='DF')  # Field name made lowercase.
    dr = models.SmallIntegerField(db_column='DR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_AllAccessMask'
        unique_together = (('id', 'floor'),)


class KoneCop(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_kgs = models.OneToOneField('KoneKgs', models.DO_NOTHING, db_column='ID_KGS')  # Field name made lowercase.
    id_acesspoint = models.ForeignKey(Acesspoint, models.DO_NOTHING, db_column='ID_AcessPoint')  # Field name made lowercase.
    elevator_id = models.IntegerField()
    group_id = models.IntegerField(blank=True, null=True)
    open_timeout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kone_COP'


class KoneCopglobaldefaultaccessmask(models.Model):
    id_kgs = models.ForeignKey('KoneKgs', models.DO_NOTHING, db_column='ID_KGS')  # Field name made lowercase.
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    systemstate = models.SmallIntegerField(db_column='SystemState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_COPGlobalDefaultAccessMask'


class KoneCopspecificmask(models.Model):
    id_elevator = models.ForeignKey(KoneCop, models.DO_NOTHING, db_column='ID_Elevator')  # Field name made lowercase.
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    copspecificsystemstate = models.IntegerField(db_column='CopSpecificSystemState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_COPSpecificMask'


class KoneCopaccess(models.Model):
    id_elevator = models.OneToOneField(KoneCop, models.DO_NOTHING, db_column='ID_Elevator', primary_key=True)  # Field name made lowercase.
    id_access = models.ForeignKey(Graccess, models.DO_NOTHING, db_column='ID_Access')  # Field name made lowercase.
    floor = models.SmallIntegerField(db_column='Floor')  # Field name made lowercase.
    df = models.SmallIntegerField(db_column='DF')  # Field name made lowercase.
    dr = models.SmallIntegerField(db_column='DR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_CopAccess'
        unique_together = (('id_elevator', 'id_access'),)


class KoneDop(models.Model):
    # id = models.IntegerField(db_column='ID', unique=True)  # Field name made lowercase.
    id_kgs = models.ForeignKey('KoneKgs', models.DO_NOTHING, db_column='ID_KGS')  # Field name made lowercase.
    id_acesspoint = models.ForeignKey(Acesspoint, models.DO_NOTHING, db_column='ID_AcessPoint')  # Field name made lowercase.
    dop_id = models.IntegerField()
    dop_floor_id = models.IntegerField()
    open_timeout = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kone_DOP'
        unique_together = (('dop_id', 'dop_floor_id', 'id_kgs'),)


class KoneDopglobaldefaultaccessmask(models.Model):
    id_kgs = models.ForeignKey('KoneKgs', models.DO_NOTHING, db_column='ID_KGS')  # Field name made lowercase.
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    systemstate = models.SmallIntegerField(db_column='SystemState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_DOPGlobalDefaultAccessMask'


class KoneDopspecificmask(models.Model):
    id_dop = models.ForeignKey(KoneDop, models.DO_NOTHING, db_column='ID_DOP')  # Field name made lowercase.
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dopspecificsystemstate = models.SmallIntegerField(db_column='DopSpecificSystemState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_DOPSpecificMask'


class KoneDestinationaccessmask(models.Model):
    id = models.OneToOneField(KoneCopglobaldefaultaccessmask, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    floor = models.SmallIntegerField(db_column='Floor')  # Field name made lowercase.
    df = models.SmallIntegerField(db_column='DF')  # Field name made lowercase.
    dr = models.SmallIntegerField(db_column='DR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_DestinationAccessMask'
        unique_together = (('id', 'floor'),)


class KoneDopaccess(models.Model):
    id_dop = models.OneToOneField(KoneDop, models.DO_NOTHING, db_column='ID_Dop', primary_key=True)  # Field name made lowercase.
    id_access = models.ForeignKey(Graccess, models.DO_NOTHING, db_column='ID_Access')  # Field name made lowercase.
    floor = models.SmallIntegerField(db_column='Floor')  # Field name made lowercase.
    df = models.SmallIntegerField(db_column='DF')  # Field name made lowercase.
    dr = models.SmallIntegerField(db_column='DR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_DopAccess'
        unique_together = (('id_dop', 'id_access', 'floor'),)


class KoneKgs(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rslines = models.ForeignKey('Rslines', models.DO_NOTHING, db_column='RSLines_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    primaryhost = models.CharField(db_column='PrimaryHost', max_length=15, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    primaryport = models.IntegerField(db_column='PrimaryPort')  # Field name made lowercase.
    backuphost = models.CharField(db_column='BackupHost', max_length=15, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    backupport = models.IntegerField(db_column='BackupPort')  # Field name made lowercase.
    floors = models.IntegerField(db_column='Floors', blank=True, null=True)  # Field name made lowercase.
    byteorder = models.SmallIntegerField(db_column='ByteOrder')  # Field name made lowercase.
    heartbeatouttimeout = models.IntegerField(db_column='HeartBeatOutTimeOut')  # Field name made lowercase.
    heartbeatintimeout = models.IntegerField(db_column='HeartBeatInTimeOut')  # Field name made lowercase.
    reconnecttimeout = models.IntegerField(db_column='ReConnectTimeOut')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kone_KGS'


class Linesbroadcast(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventgroupid = models.IntegerField(db_column='EventGroupID')  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID')  # Field name made lowercase.
    phonesid = models.IntegerField(db_column='PhonesId', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LinesBroadcast'


class Listcomponents(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    typepage = models.IntegerField(db_column='TypePage')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListComponents'


class Mapelements(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table = models.IntegerField()
    map_id = models.IntegerField()
    item_id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    rotate = models.FloatField()
    scale = models.FloatField()
    state_name = models.CharField(max_length=80, db_collation='Cyrillic_General_CI_AS')
    item_type = models.IntegerField()
    item_color = models.IntegerField()
    value_off = models.IntegerField()
    value_pos = models.IntegerField()
    text_off = models.IntegerField()
    text_pos = models.IntegerField()
    value_x = models.FloatField()
    value_y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'MapElements'


class Mapelementslinks(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mapelementsid = models.IntegerField(db_column='MapElementsID')  # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'MapElementsLinks'


class Mapelementsregions(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mapelementsid = models.IntegerField(db_column='MapElementsID')  # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'MapElementsRegions'


class Mapindicatorsdefault(models.Model):
    id_indicator = models.IntegerField(db_column='ID_Indicator', primary_key=True)  # Field name made lowercase.
    rangemin = models.FloatField(db_column='RangeMin')  # Field name made lowercase.
    rangemax = models.FloatField(db_column='RangeMax')  # Field name made lowercase.
    rangecolor = models.IntegerField(db_column='RangeColor')  # Field name made lowercase.
    statusrange = models.IntegerField(db_column='StatusRange')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MapIndicatorsDefault'
        unique_together = (('id_indicator', 'rangemin', 'rangemax'),)


class Mapinfomarker(models.Model):
    id_mapinfmark = models.AutoField(db_column='ID_MapInfMark', primary_key=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    image = models.BinaryField(db_column='Image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MapInfoMarker'


class MapElm(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mapid = models.IntegerField(db_column='MapID')  # Field name made lowercase.
    gtype = models.IntegerField(db_column='GType')  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID')  # Field name made lowercase.
    picturecount = models.IntegerField(db_column='PictureCount', blank=True, null=True)  # Field name made lowercase.
    pictures = models.BinaryField(db_column='Pictures', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    link2obj = models.IntegerField(db_column='Link2Obj', blank=True, null=True)  # Field name made lowercase.
    applicationguid = models.CharField(db_column='ApplicationGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Map_Elm'
        unique_together = (('mapid', 'gtype', 'unitid'),)


class Masterslave(models.Model):
    mastertype = models.IntegerField(db_column='MasterType', primary_key=True)  # Field name made lowercase.
    slavetype = models.IntegerField(db_column='SlaveType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterSlave'
        unique_together = (('mastertype', 'slavetype'),)


class Noderepl(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nodeid = models.IntegerField(db_column='NodeID')  # Field name made lowercase.
    scriptid = models.IntegerField(db_column='ScriptID')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NodeRepl'


class Pcompany(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_number_company = models.CharField(db_column='Id_Number_Company', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isguest = models.IntegerField(db_column='IsGuest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PCompany'

    def __str__(self):
        return '{}'.format(self.name)


class Pdivision(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shedule = models.IntegerField(db_column='Shedule', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    pcompany_id = models.IntegerField(db_column='PCompany_ID', blank=True, null=True)  # Field name made lowercase.
    id_number_division = models.CharField(db_column='ID_Number_Division', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_owner_division = models.IntegerField(db_column='ID_Owner_Division', blank=True, null=True)  # Field name made lowercase.
    patterns_id = models.IntegerField(db_column='Patterns_ID', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PDivision'


class Ppost(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    statusmark = models.IntegerField(db_column='StatusMark', blank=True, null=True)  # Field name made lowercase.
    company_id = models.IntegerField(db_column='Company_ID', blank=True, null=True)  # Field name made lowercase.
    id_number_ppost = models.CharField(db_column='Id_Number_Ppost', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PPost'


class Preason(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PReason'


class Prooms(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRooms'


class Personsphotos(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    personid = models.IntegerField(db_column='PersonID')  # Field name made lowercase.
    photodescriptor = models.BinaryField(db_column='PhotoDescriptor', blank=True, null=True)  # Field name made lowercase.
    descriptortype = models.IntegerField(db_column='DescriptorType', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    photonum = models.IntegerField(db_column='PhotoNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonsPhotos'


class Profiles(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProFiles'


class Querylog(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timeval = models.DateTimeField(db_column='TimeVal', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    query = models.CharField(db_column='Query', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    parameters = models.BinaryField(db_column='Parameters', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QueryLog'

    def __str__(self):
        return '{}'.format(self.query)


class Rsbioaccess(models.Model):
    id_devicetype = models.IntegerField(db_column='ID_DeviceType')  # Field name made lowercase.
    id_readertypeavailable = models.IntegerField(db_column='ID_ReaderTypeAvailable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSBioAccess'


class Rsbioaccess2(models.Model):
    id_devicetype = models.IntegerField(db_column='ID_DeviceType')  # Field name made lowercase.
    id_readertypeavailable = models.IntegerField(db_column='ID_ReaderTypeAvailable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSBioAccess2'


class Rsbioparams(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_device = models.ForeignKey('Rslines', models.DO_NOTHING, db_column='ID_Device')  # Field name made lowercase.
    id_param = models.ForeignKey('Pbioparams', models.DO_NOTHING, db_column='ID_Param')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSBioParams'


class Rslines(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', unique=True)  # Field name made lowercase.
    comportid = models.IntegerField(db_column='ComPortID')  # Field name made lowercase.
    pkuid = models.IntegerField(db_column='PKUID')  # Field name made lowercase.
    glineno = models.IntegerField(db_column='GLineNo')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    broadcast = models.IntegerField(db_column='Broadcast', blank=True, null=True)  # Field name made lowercase.
    deviceversion = models.IntegerField(db_column='DeviceVersion', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    macaddress = models.CharField(db_column='MACAddress', max_length=18, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    submask = models.CharField(db_column='SUBMASK', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    usedhcp = models.IntegerField(db_column='UseDHCP', blank=True, null=True)  # Field name made lowercase.
    idcontactname = models.CharField(db_column='IdContactName', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iddevice = models.IntegerField(db_column='IdDevice', blank=True, null=True)  # Field name made lowercase.
    deviceinterface = models.IntegerField(db_column='DeviceInterface')  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True, null=True)  # Field name made lowercase.
    devicetypebio = models.CharField(db_column='DeviceTypeBIO', max_length=8, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    abonenttype = models.IntegerField(db_column='AbonentType', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RSLines'
        unique_together = (('comportid', 'pkuid', 'glineno'),)


class Rdraccesspoint(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    readerid = models.IntegerField(db_column='ReaderID')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode')  # Field name made lowercase.
    accesspointid = models.IntegerField(db_column='AccessPointID')  # Field name made lowercase.
    modeacess = models.IntegerField(db_column='ModeAcess')  # Field name made lowercase.
    penalid = models.IntegerField(db_column='PenalID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RdrAccessPoint'
        unique_together = (('readerid', 'accesspointid', 'mode', 'penalid'),)


class Reasons(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID')  # Field name made lowercase.
    datestart = models.DateTimeField(db_column='DateStart', blank=True, null=True)  # Field name made lowercase.
    dateend = models.DateTimeField(db_column='DateEnd', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timestart = models.DateTimeField(db_column='TimeStart', blank=True, null=True)  # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TimeEnd', blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodtime = models.IntegerField(db_column='GoodTime', blank=True, null=True)  # Field name made lowercase.
    butnotcalc = models.IntegerField(db_column='BUTNOTCALC', blank=True, null=True)  # Field name made lowercase.
    duration = models.DateTimeField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    reasonid = models.IntegerField(db_column='ReasonID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reasons'


class Referencecommandscenarios(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    latname = models.CharField(db_column='LatName', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pprogvalue = models.TextField(db_column='PProgValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ReferenceCommandScenarios'


class Referenceitemsscenarios(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    latname = models.CharField(db_column='LatName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typevalue = models.CharField(db_column='TypeValue', max_length=10, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    typecontrl = models.CharField(db_column='TypeContrl', max_length=10, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regexp = models.CharField(db_column='RegExp', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maxvalue = models.DecimalField(db_column='MaxValue', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minvalue = models.DecimalField(db_column='MinValue', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isrefresh = models.BooleanField(db_column='isRefresh')  # Field name made lowercase.
    exptext = models.CharField(db_column='ExpText', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    increment = models.DecimalField(db_column='Increment', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    incrfixed = models.BooleanField(db_column='IncrFixed')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceItemsScenarios'


class Referencescenariostypes(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    latname = models.CharField(db_column='LatName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    def_field = models.BooleanField(db_column='Def')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    sort = models.IntegerField(db_column='Sort')  # Field name made lowercase.
    imageindex = models.IntegerField(db_column='ImageIndex')  # Field name made lowercase.
    imageidscen = models.IntegerField(db_column='ImageIDScen')  # Field name made lowercase.
    imageidstep = models.IntegerField(db_column='ImageIDStep')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceScenariosTypes'


class Referencetactics(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    latname = models.CharField(db_column='LatName', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceTactics'


class Relprof(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idlistcomp = models.ForeignKey(Listcomponents, models.DO_NOTHING, db_column='IDListComp')  # Field name made lowercase.
    idprofiles = models.ForeignKey(Profiles, models.DO_NOTHING, db_column='IDProfiles')  # Field name made lowercase.
    reserve = models.IntegerField(db_column='Reserve', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelProf'


class Relatedcameras(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cameraid = models.IntegerField(db_column='CameraID')  # Field name made lowercase.
    relatedcameraid = models.IntegerField(db_column='RelatedCameraID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedCameras'


class Relationdiv(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idauth = models.ForeignKey(Authorities, models.DO_NOTHING, db_column='IdAuth')  # Field name made lowercase.
    iddiv = models.IntegerField(db_column='IdDiv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelationDiv'


class Relationslistcar(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idlist = models.ForeignKey('Plist', models.DO_NOTHING, db_column='IdList')  # Field name made lowercase.
    idcar = models.ForeignKey('Pcar', models.DO_NOTHING, db_column='IdCar')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelationsListCar'


class Remotecontrolcategories(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    remoteaction = models.IntegerField(db_column='RemoteAction', blank=True, null=True)  # Field name made lowercase.
    groupbycategoryid = models.IntegerField(db_column='GroupByCategoryId', blank=True, null=True)  # Field name made lowercase.
    isvisibleinpersonalarea = models.IntegerField(db_column='IsVisibleInPersonalArea', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RemoteControlCategories'


class Remotecontrolcategorytodtypeselement(models.Model):
    dtypeselementid = models.IntegerField(db_column='dTypesElementId', primary_key=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RemoteControlCategoryToDTypesElement'
        unique_together = (('dtypeselementid', 'categoryid'),)


class Reservline(models.Model):
    computerid = models.IntegerField(db_column='ComputerId')  # Field name made lowercase.
    mainid = models.IntegerField(db_column='MainId', primary_key=True)  # Field name made lowercase.
    reservid = models.IntegerField(db_column='ReservId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReservLine'
        unique_together = (('mainid', 'reservid'),)


class Sslcertificate(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rootca = models.BinaryField(db_column='RootCA', blank=True, null=True)  # Field name made lowercase.
    cakey = models.BinaryField(db_column='CAKey', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    reserv = models.IntegerField(db_column='Reserv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SSLCertificate'


class Scandoc(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idplist = models.IntegerField(db_column='IDPLIST')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    spack = models.IntegerField(db_column='Spack')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScanDoc'
        unique_together = (('id', 'idplist', 'spack'),)


class Scenariosdevice(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    id_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='ID_Parent', blank=True, null=True)  # Field name made lowercase.
    id_scenariostypes = models.ForeignKey(Referencescenariostypes, models.DO_NOTHING, db_column='ID_ScenariosTypes')  # Field name made lowercase.
    id_device = models.IntegerField(db_column='ID_Device')  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType')  # Field name made lowercase.
    id_level = models.IntegerField(db_column='ID_Level')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScenariosDevice'


class Scenariosfilterdevice(models.Model):
    devicetype = models.IntegerField(db_column='DeviceType', primary_key=True)  # Field name made lowercase.
    elementtype = models.IntegerField(db_column='ElementType')  # Field name made lowercase.
    id_scenariostype = models.ForeignKey(Referencescenariostypes, models.DO_NOTHING, db_column='ID_ScenariosType')  # Field name made lowercase.
    deviceversion = models.IntegerField(db_column='DeviceVersion')  # Field name made lowercase.
    numberdevitem = models.IntegerField(db_column='NumberDevItem')  # Field name made lowercase.
    parentdevtype = models.IntegerField(db_column='ParentDevType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScenariosFilterDevice'
        unique_together = (('devicetype', 'elementtype', 'deviceversion', 'id_scenariostype', 'parentdevtype', 'numberdevitem'),)


class Schedule(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    scriptid = models.IntegerField(db_column='ScriptID', blank=True, null=True)  # Field name made lowercase.
    calendar = models.BinaryField(db_column='Calendar', blank=True, null=True)  # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'


class Script(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hotkey = models.IntegerField(db_column='HotKey', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    content = models.BinaryField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Script'


class Settings(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    settings = models.BinaryField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Settings'


class SettingsValue(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    id_comp = models.IntegerField()
    groups = models.ForeignKey('SettingsGroup', models.DO_NOTHING, db_column='Groups_Id')  # Field name made lowercase.
    settings = models.BinaryField(blank=True, null=True)
    value = models.CharField(db_column='Value', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    typevalue = models.IntegerField(db_column='TypeValue')  # Field name made lowercase.
    reserve = models.IntegerField(db_column='Reserve', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Settings_Value'


class SettingsGroup(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Settings_group'


class Smsgatesparams(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    passw = models.CharField(db_column='Passw', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inboundphone = models.CharField(db_column='InboundPhone', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rslinesid = models.IntegerField(db_column='RsLinesId')  # Field name made lowercase.
    proxyserver = models.CharField(db_column='ProxyServer', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    proxyport = models.IntegerField(db_column='ProxyPort')  # Field name made lowercase.
    proxylogin = models.CharField(db_column='ProxyLogin', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    proxypassw = models.CharField(db_column='ProxyPassw', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SmsGatesParams'


class Sys(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    minvalue = models.IntegerField(db_column='MinValue')  # Field name made lowercase.
    maxvalue = models.IntegerField(db_column='MaxValue')  # Field name made lowercase.
    defaultvalue = models.IntegerField(db_column='DefaultValue')  # Field name made lowercase.
    required = models.IntegerField(db_column='Required')  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    hint = models.CharField(db_column='Hint', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    list = models.BinaryField(db_column='List', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    sysorder = models.IntegerField(db_column='SysOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sys'


class Sysgroup(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    sysorder = models.IntegerField(db_column='SysOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SysGroup'


class Sysparam(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype', blank=True, null=True)  # Field name made lowercase.
    gvalue = models.IntegerField(db_column='GValue', blank=True, null=True)  # Field name made lowercase.
    required = models.IntegerField(db_column='Required', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SysParam'


class Systemobjects(models.Model):
    gindex = models.IntegerField(db_column='GIndex', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    exstate = models.IntegerField(db_column='ExState')  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime')  # Field name made lowercase.
    reserve1 = models.IntegerField(db_column='Reserve1')  # Field name made lowercase.
    reserve2 = models.IntegerField(db_column='Reserve2')  # Field name made lowercase.
    reserve3 = models.IntegerField(db_column='Reserve3')  # Field name made lowercase.
    reserve4 = models.IntegerField(db_column='Reserve4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SystemObjects'
        unique_together = (('gindex', 'type'),)


class Timecont(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeID')  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeCont'


class Timetable(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    worktimezoneid = models.IntegerField(db_column='WorkTimeZoneID')  # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeID')  # Field name made lowercase.
    config = models.IntegerField(db_column='Config')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeTable'


class Treectrl(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    absoluteindex = models.IntegerField(db_column='AbsoluteIndex')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    glevel = models.IntegerField(db_column='GLevel')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreeCtrl'


class Treenode(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    icon = models.IntegerField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    special = models.IntegerField(db_column='Special', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreeNode'


class Typedoclist(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    indentsh = models.CharField(db_column='IndentSh', max_length=250, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    numbertype = models.IntegerField(db_column='NumberType')  # Field name made lowercase.
    sibstringname = models.CharField(db_column='SibStringName', max_length=250, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    numinlist = models.IntegerField(db_column='NumInList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeDocList'


class Typeshldevice(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType')  # Field name made lowercase.
    devicetypename = models.CharField(db_column='DeviceTypeName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deviceversion = models.IntegerField(db_column='DeviceVersion', blank=True, null=True)  # Field name made lowercase.
    numshbegin = models.IntegerField(db_column='NumShBegin', blank=True, null=True)  # Field name made lowercase.
    numshstop = models.IntegerField(db_column='NumShStop', blank=True, null=True)  # Field name made lowercase.
    elementtype = models.IntegerField(db_column='ElementType', blank=True, null=True)  # Field name made lowercase.
    shltype = models.IntegerField(db_column='ShlType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TypeShlDevice'


class Valuedevitemsscenarios(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_device = models.IntegerField(db_column='ID_Device', primary_key=True)  # Field name made lowercase.
    id_devicetype = models.IntegerField(db_column='ID_DeviceType')  # Field name made lowercase.
    id_refitemsscen = models.ForeignKey(Referenceitemsscenarios, models.DO_NOTHING, db_column='ID_RefItemsScen')  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ValueDevItemsScenarios'
        unique_together = (('id_device', 'id_devicetype', 'id_refitemsscen'),)


class Valueitemsscenarios(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    id_scendevice = models.OneToOneField(Scenariosdevice, models.DO_NOTHING, db_column='ID_ScenDevice', primary_key=True)  # Field name made lowercase.
    id_refitemsscen = models.ForeignKey(Referenceitemsscenarios, models.DO_NOTHING, db_column='ID_RefItemsScen')  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ValueItemsScenarios'
        unique_together = (('id_scendevice', 'id_refitemsscen'),)


class Versiondb(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=10, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    versiondatabase = models.CharField(db_column='VersionDataBase', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    counttable = models.IntegerField(db_column='CountTable')  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=40, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    rezerv1 = models.IntegerField(db_column='Rezerv1')  # Field name made lowercase.
    guid_db = models.CharField(db_column='GUID_DB', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VersionDB'


class Videoarchive(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=256, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    objtype = models.IntegerField(db_column='ObjType')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    param = models.IntegerField(db_column='Param', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoArchive'


class Videocamshots(models.Model):
    # id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cameraid = models.IntegerField(db_column='CameraID')  # Field name made lowercase.
    eventtime = models.DateTimeField(db_column='EventTime')  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    reserv = models.IntegerField(db_column='Reserv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoCamShots'


class Videoevents(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    typeobj = models.IntegerField(db_column='TypeObj')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    event = models.IntegerField(db_column='Event')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FileSize')  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    param = models.IntegerField(db_column='Param', blank=True, null=True)  # Field name made lowercase.
    pathid = models.CharField(db_column='PathID', max_length=36)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NumRec', blank=True, null=True)  # Field name made lowercase.
    numpart = models.IntegerField(db_column='NumPart', blank=True, null=True)  # Field name made lowercase.
    protectedrec = models.SmallIntegerField(db_column='ProtectedRec', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoEvents'


class Videorecognizeaccesspoint(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    readerid = models.IntegerField(db_column='ReaderID')  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode')  # Field name made lowercase.
    accesspointid = models.IntegerField(db_column='AccessPointID')  # Field name made lowercase.
    modeaccess = models.IntegerField(db_column='ModeAccess')  # Field name made lowercase.
    readermode = models.IntegerField(db_column='ReaderMode')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoRecognizeAccessPoint'


class Videorecognizechannels(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    videoinspectorid = models.IntegerField(db_column='VideoInspectorID')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    profileid = models.IntegerField(db_column='ProfileID')  # Field name made lowercase.
    cameraid = models.IntegerField(db_column='CameraID')  # Field name made lowercase.
    channelmode = models.IntegerField(db_column='ChannelMode', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoRecognizeChannels'


class Videorecognizeprofiles(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    settings = models.BinaryField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VideoRecognizeProfiles'


class Worktimezone(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTimeZone'


class Adc(models.Model):
    timeval = models.DateTimeField(db_column='TimeVal', blank=True, null=True)  # Field name made lowercase.
    indexzone = models.IntegerField(db_column='IndexZone', blank=True, null=True)  # Field name made lowercase.
    indexdevice = models.IntegerField(db_column='IndexDevice', blank=True, null=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID', blank=True, null=True)  # Field name made lowercase.
    logid = models.IntegerField(db_column='LogID', blank=True, null=True)  # Field name made lowercase.
    adc = models.FloatField(db_column='ADC', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    typeadc = models.IntegerField(db_column='TypeAdc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adc'


class Dtypes(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countshl = models.IntegerField(db_column='CountShl', blank=True, null=True)  # Field name made lowercase.
    countkey = models.IntegerField(db_column='CountKey', blank=True, null=True)  # Field name made lowercase.
    countreader = models.IntegerField(db_column='CountReader', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    face = models.IntegerField(db_column='Face', blank=True, null=True)  # Field name made lowercase.
    icon = models.IntegerField(db_column='Icon', blank=True, null=True)  # Field name made lowercase.
    protokoltype = models.IntegerField(db_column='ProtokolType', blank=True, null=True)  # Field name made lowercase.
    interfaces = models.IntegerField(db_column='Interfaces', blank=True, null=True)  # Field name made lowercase.
    worklib = models.CharField(db_column='WorkLib', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dTypes'


class Dtypeselement(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='DeviceType')  # Field name made lowercase.
    deviceversion = models.IntegerField(db_column='DeviceVersion', blank=True, null=True)  # Field name made lowercase.
    elementtype = models.IntegerField(db_column='ElementType', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    countshl = models.IntegerField(db_column='CountShl')  # Field name made lowercase.
    countkey = models.IntegerField(db_column='CountKey')  # Field name made lowercase.
    countreader = models.IntegerField(db_column='CountReader')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    eventgroupid = models.IntegerField(db_column='EventGroupID')  # Field name made lowercase.
    deviceversionstr = models.CharField(db_column='DeviceVersionStr', max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    property = models.IntegerField(db_column='Property', blank=True, null=True)  # Field name made lowercase.
    elementstypesgroupid = models.IntegerField(db_column='ElementsTypesGroupId', blank=True, null=True)  # Field name made lowercase.
    sortingnum = models.IntegerField(db_column='SortingNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dTypesElement'


class Devicemasterslave(models.Model):
    mastertype = models.IntegerField(primary_key=True)
    slavetype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'devicemasterslave'
        unique_together = (('mastertype', 'slavetype'),)


class Drivers(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    port = models.IntegerField()
    ip = models.CharField(db_column='IP', max_length=15, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    mac = models.CharField(max_length=18, db_collation='Cyrillic_General_CI_AS')
    files = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    mainfile = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    inifile = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    parameters = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')
    start_cmd = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    stop_cmd = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    install_cmd = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    uninstall_cmd = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')
    folder = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'drivers'


class DriversComps(models.Model):
    id_computer = models.IntegerField(primary_key=True)
    id_driver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drivers_comps'
        unique_together = (('id_computer', 'id_driver'),)


class Interfaceprotocol(models.Model):
    interface_id = models.IntegerField(primary_key=True)
    protocol_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interfaceprotocol'
        unique_together = (('interface_id', 'protocol_id'),)


class Interfaces(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'interfaces'


class ListComments(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'list_comments'


class Logs(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tpchange = models.IntegerField(db_column='tpChange', blank=True, null=True)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    computerip = models.IntegerField(db_column='ComputerIP', blank=True, null=True)  # Field name made lowercase.
    timeval = models.DateTimeField(db_column='TimeVal', blank=True, null=True)  # Field name made lowercase.
    ruquestdata = models.BinaryField(db_column='RuquestDATA', blank=True, null=True)  # Field name made lowercase.
    reserv0 = models.IntegerField(db_column='Reserv0', blank=True, null=True)  # Field name made lowercase.
    reserv1 = models.IntegerField(db_column='Reserv1', blank=True, null=True)  # Field name made lowercase.
    reserv2 = models.CharField(db_column='Reserv2', max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logs'


class LogsChangeBd(models.Model):
    id = models.UUIDField(db_column='ID', primary_key=True, max_length=36)  # Field name made lowercase.
    timeval = models.DateTimeField(db_column='timeVal')  # Field name made lowercase.
    state_record = models.IntegerField()
    table_name = models.CharField(max_length=60, db_collation='Cyrillic_General_CI_AS')
    valueid = models.IntegerField(db_column='ValueId')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorId')  # Field name made lowercase.
    insidesystem = models.CharField(db_column='InsideSystem', max_length=30, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    xml_data = models.CharField(max_length=400, db_collation='Cyrillic_General_CI_AS')
    num = models.IntegerField(db_column='Num', unique=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logs_change_bd'
        ordering = ["-timeval"]

    def __str__(self):
        return '{} {}'.format(self.table_name, self.xml_data)


class MAlarm(models.Model):
    time0 = models.DateTimeField(db_column='Time0', blank=True, null=True)  # Field name made lowercase.
    numcom = models.IntegerField(db_column='NumCom', blank=True, null=True)  # Field name made lowercase.
    idcomp = models.IntegerField(db_column='IDComp', blank=True, null=True)  # Field name made lowercase.
    operator0 = models.IntegerField(db_column='Operator0', blank=True, null=True)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='EventName', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    event = models.IntegerField(db_column='Event')  # Field name made lowercase.
    addrcom = models.IntegerField(db_column='AddrCOM', blank=True, null=True)  # Field name made lowercase.
    address = models.IntegerField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    object = models.IntegerField(db_column='Object', blank=True, null=True)  # Field name made lowercase.
    action1 = models.CharField(db_column='Action1', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time1 = models.DateTimeField(db_column='Time1', blank=True, null=True)  # Field name made lowercase.
    operator1 = models.IntegerField(db_column='Operator1', blank=True, null=True)  # Field name made lowercase.
    action2 = models.CharField(db_column='Action2', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time2 = models.DateTimeField(db_column='Time2', blank=True, null=True)  # Field name made lowercase.
    operator2 = models.IntegerField(db_column='Operator2', blank=True, null=True)  # Field name made lowercase.
    action3 = models.CharField(db_column='Action3', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time3 = models.DateTimeField(db_column='Time3', blank=True, null=True)  # Field name made lowercase.
    operator3 = models.IntegerField(db_column='Operator3', blank=True, null=True)  # Field name made lowercase.
    action4 = models.CharField(db_column='Action4', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time4 = models.DateTimeField(db_column='Time4', blank=True, null=True)  # Field name made lowercase.
    operator4 = models.IntegerField(db_column='Operator4', blank=True, null=True)  # Field name made lowercase.
    action5 = models.CharField(db_column='Action5', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time5 = models.DateTimeField(db_column='Time5', blank=True, null=True)  # Field name made lowercase.
    operator5 = models.IntegerField(db_column='Operator5', blank=True, null=True)  # Field name made lowercase.
    action6 = models.CharField(db_column='Action6', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time6 = models.DateTimeField(db_column='Time6', blank=True, null=True)  # Field name made lowercase.
    operator6 = models.IntegerField(db_column='Operator6', blank=True, null=True)  # Field name made lowercase.
    stage = models.IntegerField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.
    doorid = models.IntegerField(db_column='DoorID', blank=True, null=True)  # Field name made lowercase.
    zonetype = models.IntegerField(db_column='ZoneType', blank=True, null=True)  # Field name made lowercase.
    accesszoneindex = models.IntegerField(db_column='AccessZoneIndex', blank=True, null=True)  # Field name made lowercase.
    vevent = models.IntegerField(db_column='VEvent', blank=True, null=True)  # Field name made lowercase.
    zreserv = models.IntegerField(db_column='ZReserv', blank=True, null=True)  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    indexzone = models.IntegerField(db_column='IndexZone', blank=True, null=True)  # Field name made lowercase.
    tpindex = models.IntegerField(db_column='tpIndex', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm_alarm'


class MapIndicators(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    mapelmid = models.OneToOneField(MapElm, models.DO_NOTHING, db_column='MapElmId', primary_key=True)  # Field name made lowercase.
    range_min = models.FloatField()
    range_max = models.FloatField()
    range_color = models.IntegerField()
    status_range = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'map_indicators'
        unique_together = (('mapelmid', 'id'),)


class OrionGlobalvalues(models.Model):
    id_value = models.CharField(primary_key=True, max_length=25, db_collation='Cyrillic_General_CI_AS')
    value = models.CharField(max_length=250, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'orion_globalValues'


class Pbioaccess(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pmark = models.ForeignKey('Pmark', models.DO_NOTHING, db_column='ID_pMark')  # Field name made lowercase.
    gtype = models.IntegerField(db_column='GType')  # Field name made lowercase.
    biotemplate2 = models.TextField(db_column='BioTemplate2', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pBioAccess'


class Pbioparams(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    device_type = models.IntegerField(db_column='Device_Type')  # Field name made lowercase.
    master = models.IntegerField(db_column='Master')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=128, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    defvalue = models.CharField(db_column='DefValue', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    values = models.CharField(db_column='Values', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pBioParams'


class Pcar(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    vin = models.CharField(db_column='Vin', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pCar'


class Pgroupexit(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAme', max_length=150, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pGroupExit'


class Plist(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=25, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    midname = models.CharField(db_column='MidName', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    company = models.ForeignKey(Pcompany, models.DO_NOTHING, db_column='Company', blank=True, null=True)  # Field name made lowercase.
    section = models.IntegerField(db_column='Section', blank=True, null=True)  # Field name made lowercase.
    post = models.ForeignKey(Ppost, models.DO_NOTHING, db_column='Post', blank=True, null=True)  # Field name made lowercase.
    schedule = models.IntegerField(db_column='Schedule', blank=True, null=True)  # Field name made lowercase.
    avto = models.CharField(db_column='Avto', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    spack = models.IntegerField(db_column='Spack', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    tabnumber = models.CharField(db_column='TabNumber', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grstatus = models.IntegerField(db_column='GrStatus', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime', blank=True, null=True)  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True, null=True)  # Field name made lowercase.
    statusrecord = models.IntegerField(db_column='StatusRecord', blank=True, null=True)  # Field name made lowercase.
    patterns_id = models.IntegerField(db_column='Patterns_ID', blank=True, null=True)  # Field name made lowercase.
    id_number_list = models.CharField(db_column='ID_Number_List', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    delta_weight = models.IntegerField(blank=True, null=True)
    autoid = models.IntegerField(db_column='AutoID', blank=True, null=True)  # Field name made lowercase.
    guid_1c = models.CharField(db_column='GUID_1C', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status_list = models.IntegerField(blank=True, null=True)
    emaillist = models.CharField(db_column='EmailList', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fielddelete = models.IntegerField(blank=True, null=True)
    blacklist = models.IntegerField(db_column='BlackList', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reasontoblacklist = models.CharField(db_column='ReasonToBlackList', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typedocum = models.IntegerField(db_column='TypeDocum', blank=True, null=True)  # Field name made lowercase.
    sexguest = models.IntegerField(db_column='SexGuest', blank=True, null=True)  # Field name made lowercase.
    dokumseries = models.CharField(db_column='DokumSeries', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dokumnumber = models.CharField(db_column='DokumNumber', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datedocument = models.DateTimeField(db_column='DateDocument', blank=True, null=True)  # Field name made lowercase.
    kodpodr = models.CharField(db_column='KodPodr', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kem = models.CharField(db_column='Kem', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datedocumentend = models.DateTimeField(db_column='DateDocumentEnd', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    datetimeinarchive = models.DateTimeField(db_column='DateTimeInArchive', blank=True, null=True)  # Field name made lowercase.
    firetolist = models.CharField(db_column='FireToList', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idscan = models.IntegerField(db_column='IDSCAN', blank=True, null=True)  # Field name made lowercase.
    idgroupexit = models.IntegerField(db_column='IDGROUPEXIT', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    roomid = models.IntegerField(db_column='RoomID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pList'
        ordering = ['name']

    def __str__(self):
        return '{} {} {}'.format(self.name, self.firstname, self.midname)


class Plistnetports(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name_task = models.CharField(db_column='NAME_TASK', max_length=40, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    port_task = models.IntegerField(db_column='PORT_TASK', unique=True, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pListNetPorts'


class Plogdata(models.Model):
    timeval = models.DateTimeField(db_column='TimeVal')  # Field name made lowercase.
    numcom = models.IntegerField(db_column='NumCom', blank=True, null=True)  # Field name made lowercase.
    idcomp = models.IntegerField(db_column='IDComp', blank=True, null=True)  # Field name made lowercase.
    par1 = models.IntegerField(db_column='Par1', blank=True, null=True)  # Field name made lowercase.
    par2 = models.IntegerField(db_column='Par2', blank=True, null=True)  # Field name made lowercase.
    par3 = models.IntegerField(db_column='Par3', blank=True, null=True)  # Field name made lowercase.
    par4 = models.IntegerField(db_column='Par4', blank=True, null=True)  # Field name made lowercase.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event')  # Field name made lowercase.
    indexkey = models.IntegerField(db_column='IndexKey', blank=True, null=True)  # Field name made lowercase.
    razdindex = models.IntegerField(db_column='RazdIndex', blank=True, null=True)  # Field name made lowercase.
    hozorgan = models.ForeignKey(Plist, models.DO_NOTHING, db_column='HozOrgan', blank=True, null=True)  # Field name made lowercase.
    hozguest = models.IntegerField(db_column='HozGuest', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=65, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doorindex = models.IntegerField(db_column='DoorIndex', blank=True, null=True)  # Field name made lowercase.
    mode = models.IntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    devicetime = models.DateTimeField(db_column='DeviceTime', blank=True, null=True)  # Field name made lowercase.
    vevent = models.IntegerField(db_column='VEvent', blank=True, null=True)  # Field name made lowercase.
    zreserv = models.IntegerField(db_column='ZReserv', blank=True, null=True)  # Field name made lowercase.
    zoneindex = models.IntegerField(db_column='ZoneIndex', blank=True, null=True)  # Field name made lowercase.
    readerindex = models.IntegerField(db_column='ReaderIndex', blank=True, null=True)  # Field name made lowercase.
    sign = models.IntegerField(db_column='Sign', blank=True, null=True)  # Field name made lowercase.
    tprzdindex = models.IntegerField(db_column='tpRzdIndex', blank=True, null=True)  # Field name made lowercase.
    tppar4 = models.IntegerField(db_column='tpPar4', blank=True, null=True)  # Field name made lowercase.
    indexzone = models.IntegerField(db_column='IndexZone', blank=True, null=True)  # Field name made lowercase.
    tpindex = models.IntegerField(db_column='tpIndex', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    idcomment = models.IntegerField(db_column='IdComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pLogData'
        ordering = ['devicetime']

    def __str__(self):
        return '{}'.format(self.devicetime)


class Pmaps(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    planchild = models.IntegerField(db_column='PlanChild', blank=True, null=True)  # Field name made lowercase.
    spack = models.IntegerField(db_column='Spack', blank=True, null=True)  # Field name made lowercase.
    contents = models.BinaryField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime', blank=True, null=True)  # Field name made lowercase.
    design_width = models.IntegerField(blank=True, null=True)
    design_height = models.IntegerField(blank=True, null=True)
    design_scale = models.FloatField(blank=True, null=True)
    schemaext = models.CharField(db_column='SchemaExt', max_length=5, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    applicationguid = models.CharField(db_column='ApplicationGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pMaps'


class Pmark(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gtype = models.IntegerField(db_column='Gtype')  # Field name made lowercase.
    gtypecodeadd = models.IntegerField(db_column='GTypeCodeAdd', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config')  # Field name made lowercase.
    codep = models.CharField(db_column='CodeP', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codepadd = models.CharField(db_column='CodePAdd', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner')  # Field name made lowercase.
    ownername = models.CharField(db_column='OwnerName', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grstatus = models.IntegerField(db_column='GrStatus', blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    finish = models.DateTimeField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    fingertemplate = models.CharField(max_length=2500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    indexforcontactid = models.IntegerField(db_column='IndexForContactId', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=250, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pMark'


class Pobjcont(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectID')  # Field name made lowercase.
    shleifid = models.IntegerField(db_column='ShleifID')  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='ItemType')  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pObjCont'
        unique_together = (('objectid', 'shleifid', 'itemtype'),)


class Pobjects(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    simindex = models.CharField(db_column='SimIndex', max_length=1, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    config = models.IntegerField(db_column='Config', blank=True, null=True)  # Field name made lowercase.
    alarmkey = models.IntegerField(db_column='AlarmKey', blank=True, null=True)  # Field name made lowercase.
    guardkey = models.IntegerField(db_column='GuardKey', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elementstypesgroupid = models.IntegerField(db_column='ElementsTypesGroupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pObjects'
        unique_together = (('computerid', 'gindex'),)


class PhoneNumbers(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    phone_number = models.CharField(max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    ip = models.CharField(max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    translateprotocol = models.IntegerField(db_column='translateProtocol', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=5, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    description = models.CharField(max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone_numbers'


class Protocoldevices(models.Model):
    protocol_id = models.IntegerField(primary_key=True)
    device_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'protocoldevices'
        unique_together = (('protocol_id', 'device_type_id'),)


class Protocols(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'protocols'


class RelationPhoneIdDev(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_phone = models.IntegerField()
    id_rslines = models.IntegerField()
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relation_phone_id_dev'
        unique_together = (('id_phone', 'id_rslines'),)


class StatesItem(models.Model):
    item_type = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    tmvl = models.DateTimeField()
    state_item = models.IntegerField(blank=True, null=True)
    comps_id = models.IntegerField(blank=True, null=True)
    id_owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states_item'
        unique_together = (('item_type', 'item_id'),)


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Cyrillic_General_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tkbpenals(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    id_section = models.IntegerField(db_column='ID_Section')  # Field name made lowercase.
    bindex = models.IntegerField(db_column='BIndex')  # Field name made lowercase.
    box_name = models.CharField(db_column='Box_Name', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactID', blank=True, null=True)  # Field name made lowercase.
    plistid = models.IntegerField(db_column='pListID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tKBPenals'


class Tkbsections(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_keybox = models.IntegerField(db_column='ID_Keybox')  # Field name made lowercase.
    stype = models.IntegerField(db_column='SType')  # Field name made lowercase.
    rows = models.IntegerField(db_column='Rows', blank=True, null=True)  # Field name made lowercase.
    columns = models.IntegerField(db_column='Columns', blank=True, null=True)  # Field name made lowercase.
    secno = models.IntegerField(db_column='SecNo', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tKBSections'


class Tkeyboxes(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex')  # Field name made lowercase.
    idcomport = models.IntegerField(db_column='IdComPort')  # Field name made lowercase.
    adress = models.IntegerField(db_column='Adress', blank=True, null=True)  # Field name made lowercase.
    devname = models.CharField(db_column='DevName', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sectionsqty = models.IntegerField(db_column='SectionsQTY')  # Field name made lowercase.
    ver = models.CharField(db_column='Ver', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    compid = models.IntegerField(db_column='CompID')  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=16, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    accesskey = models.CharField(db_column='AccessKey', max_length=27, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    indexforcontactid = models.IntegerField(db_column='IndexForContactID', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tKeyBoxes'


class Tpstufflogdata(models.Model):
    guid = models.CharField(db_column='GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    penalid = models.IntegerField(db_column='PenalID')  # Field name made lowercase.
    plistid = models.IntegerField(db_column='PListID')  # Field name made lowercase.
    referencebookid = models.IntegerField(db_column='ReferenceBookID')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=240, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timeval = models.DateTimeField(db_column='TimeVal')  # Field name made lowercase.
    fio = models.CharField(db_column='FIO', max_length=200, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pstuffname = models.CharField(db_column='PStuffName', max_length=240, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPStuffLogData'


class Tpstuffphoto(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idplist = models.ForeignKey(Plist, models.DO_NOTHING, db_column='IDPLIST')  # Field name made lowercase.
    picture = models.BinaryField(blank=True, null=True)
    spack = models.IntegerField(db_column='Spack', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPStuffPhoto'


class Tpersonalstuff(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    plistid = models.ForeignKey(Plist, models.DO_NOTHING, db_column='PListID')  # Field name made lowercase.
    penalid = models.IntegerField(db_column='PenalID')  # Field name made lowercase.
    referencebookid = models.ForeignKey('Treferencebook', models.DO_NOTHING, db_column='ReferenceBookID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPersonalStuff'


class Treferencebook(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='RefType', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=150, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tReferenceBook'


class Vinsp(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    computerid = models.IntegerField(db_column='ComputerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tcp_ip = models.CharField(db_column='TCP_IP', max_length=15, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vinsptype = models.IntegerField(db_column='VinspType', blank=True, null=True)  # Field name made lowercase.
    activex = models.IntegerField(db_column='ActiveX', blank=True, null=True)  # Field name made lowercase.
    compname = models.CharField(db_column='CompName', max_length=30, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gindex = models.IntegerField(db_column='GIndex', blank=True, null=True)  # Field name made lowercase.
    vinspparams = models.CharField(db_column='vInspParams', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    archivepath = models.CharField(db_column='ArchivePath', max_length=128, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    issecure = models.IntegerField(db_column='IsSecure', blank=True, null=True)  # Field name made lowercase.
    settings = models.BinaryField(db_column='Settings', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='Workstation', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vInsp'


class Vinsptypes(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vinsptype = models.IntegerField(db_column='vInspType', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=80, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vInspTypes'


class Weightcamera(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    door = models.IntegerField()
    weightterminal = models.IntegerField()
    weight0 = models.IntegerField()
    weightdiscret = models.IntegerField()
    deltaweightstable = models.IntegerField()
    durationdooropen = models.IntegerField()
    durationdooropenclose = models.IntegerField()
    timefilter = models.IntegerField()
    timestep = models.IntegerField()
    minpersonweight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weightcamera'
