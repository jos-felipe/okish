#!/usr/bin/env python3

status = 0

print("\nBUILTIN UNIT TEST\n")

from echo.unit_tester import unit_echo
_status = unit_echo()
if _status != 0:
	status = 1

from builtin_cd.unit_tester import unit_cd
_status = unit_cd()
if _status != 0:
	status = 1

from builtin_pwd.unit_tester import unit_pwd
_status = unit_pwd()
if _status != 0:
	status = 1

from builtin_export.unit_tester import unit_export
_status = unit_export()
if _status != 0:
	status = 1

from builtin_unset.unit_tester import unit_unset
_status = unit_unset()
if _status != 0:
	status = 1

from builtin_env.unit_tester import unit_env
_status = unit_env()
if _status != 0:
	status = 1

from builtin_exit.unit_tester import unit_exit
_status = unit_exit()
if _status != 0:
	status = 1

print(f"Status: {status}")
exit(status)
