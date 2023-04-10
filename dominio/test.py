from OpenDominio import OpenDominio
from LoginDominio import LoginDominio

od = OpenDominio()
OpenFolha = od.open_module('folha')

login = LoginDominio()
UserROTINASDP = login.user_login(user='ROTINASDP')
PasswordROTINASDPDP = login.password_login(password='74157')
OkLogin = login.ok_login()