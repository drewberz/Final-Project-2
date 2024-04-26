#builder-generated code used to know what packages are needed
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
name = 'Path Tracing'
#generate window
win = visual.Window(size = [900, 900], pos = [0,0], fullscr = False, color = [0,0,0], allowGUI = True)
framerate = win._monitorFrameRate
win.MouseVisible = True

#From Builder code = sets up keyboard to accept responses
deviceManager = hardware.DeviceManager()

if deviceManager.getDevice('defaultKeyboard') is None:
    deviceManager.addDevice(
        deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
    )
if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
    key_resp = deviceManager.addDevice(
        deviceClass='keyboard',
        deviceName='key_resp',
    )

clock = core.Clock()
time = clock.getTime()
#create dictionary to store information about experiment
Info = {'participant': randint(0, 999), 'date':data.getDateStr()}
key_resp = keyboard.Keyboard(deviceName='key_resp')

#Instruction Page
instructions = visual.TextBox2(win, text = 'INSTRUCTIONS\nPRESS ANY KEY TO CONTINUE')
testtext = visual.TextBox2(win, text = 'NEXT')
thistrial = data.ExperimentHandler(name = name, extraInfo = Info, dataFileName = 'final_project_data')
continueRoutine = True
frameN = -1
while continueRoutine:
    instructions.draw()
    win.flip()
    keys = key_resp.getKeys()
    print(keys)
    if keys is not None:
        win.close()
        #testtext.draw()
        #win.flip



#test


