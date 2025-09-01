# Import modul dari Design
import Robot.Design.face
import Robot.Design.outfit

print(Robot.Design.face.tampilkan_wajah())
print(Robot.Design.outfit.tampilkan_pakaian())


# Import modul dari Actions
import Robot.Actions.walk
import Robot.Actions.hello

print(Robot.Actions.walk.mulai_berjalan())
print(Robot.Actions.hello.sapa())


# Import modul dari Sound
import Robot.Sound.alarm

print(Robot.Sound.alarm.bunyikan_alarm())



from Robot.Actions.hello import sapa
print(sapa())

from Robot.Sound.alarm import bunyikan_alarm
print(bunyikan_alarm())



from Robot.Design.face import *
from Robot.Actions.walk import *

print(tampilkan_wajah())
print(mulai_berjalan())