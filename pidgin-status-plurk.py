#!/usr/bin/env python

#
# Send Pidgin status to Plurk
#

# Author: Fajran Iman Rusadi
# License: Public Domain

import plurkdata
import plurkapi

import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

def send_plurk(msg):
	p = plurkapi.PlurkAPI()
	p.login(plurkdata.username, plurkdata.password)
	p.addPlurk(qualifier=':', content=msg)

def on_status_changed(new, old):
	global purple
	msg = purple.PurpleSavedstatusGetMessage(new)
	send_plurk(msg)

bus.add_signal_receiver(on_status_changed,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="SavedstatusChanged")

loop = gobject.MainLoop()
loop.run()

