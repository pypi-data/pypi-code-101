from cerver.utils.log import LOG_TYPE_NONE, cerver_log_both

from .lib import lib

PYMAGIC_VERSION = "0.2"
PYMAGIC_VERSION_NAME = "Version 0.2"
PYMAGIC_VERSION_DATE = "16/11/2021"
PYMAGIC_VERSION_TIME = "07:39 CST"
PYMAGIC_VERSION_AUTHOR = "Erick Salas"

version = {
	"id": PYMAGIC_VERSION,
	"name": PYMAGIC_VERSION_NAME,
	"date": PYMAGIC_VERSION_DATE,
	"time": PYMAGIC_VERSION_TIME,
	"author": PYMAGIC_VERSION_AUTHOR
}

magic_version_print_full = lib.magic_version_print_full
magic_version_print_version_id = lib.magic_version_print_version_id
magic_version_print_version_name = lib.magic_version_print_version_name

def pymagic_version_print_full ():
	output = "\nPyMagic Version: {name}\n" \
		"Release Date: {date} - {time}\n" \
		"Author: {author}\n".format (**version)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		output.encode ("utf-8")
	)

def pymagic_version_print_version_id ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		f"\nPyMagic Version ID: {version.id}\n".encode ("utf-8")
	)

def pymagic_version_print_version_name ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		f"\nPyMagic Version: {version.name}\n".encode ("utf-8")
	)
