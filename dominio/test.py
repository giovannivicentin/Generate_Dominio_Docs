from OpenDominio import OpenDominio
from LoginDominio import LoginDominio
from RoutineParameters import RoutineParameters

od = OpenDominio()
OpenFolha = od.open_module('folha')

login = LoginDominio()
UserROTINASDP = login.user_login(user='ROTINASDP')
PasswordROTINASDP = login.password_login(password='74157')

Param = RoutineParameters()
RoutineFolha = Param.Select_Automatic_Routines('folha_cm')
