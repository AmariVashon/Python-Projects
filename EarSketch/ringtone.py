#		python code
#		script_name: Ringtone
#
#		author: Amari Harrington
#		description: A hip hop style ringtone using a combination of drums, bass, and sound effects
#

from earsketch import *

init()
setTempo(90)
#setEffect(1, DELAY, DELAY_TIME, 400)
setEffect(3, VOLUME, GAIN, 5)

drum = CIARA_SET_DRUMBEAT_5
bass = HIPHOP_BASSSUB_005
bass2 = Y57_BASS_1
drum2 = HIPHOP_DUSTYPERCUSSION_001
bass3 = HIPHOP_BASSSUB_001

def intro():
    fitMedia(drum, 1, 1, 30)
    fitMedia(bass, 2, 1, 30)
    fitMedia(bass2, 3, 5, 30)

intro()
beat = "0-0++0-00-0+0+"
for i in range(10, 30):
    makeBeat(drum2, 4, i, beat)

def end():
    fitMedia(bass3, 5, 15, 30)
    fitMedia(Y28_TURNTABLE_1, 6, 21, 30)

end()

finish()
