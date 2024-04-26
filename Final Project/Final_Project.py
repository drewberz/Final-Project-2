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
    instructions.autoDraw = True
    win.flip()
    #keys.append(key_resp.getKeys())
    #print(keys)
    if 'space' in key_resp.getKeys():
        print('trying to close window')
        #core.quit()
        instructions.autoDraw = False
        win.flip()
        testtext.autoDraw = True
        win.flip



#test

    
#----Initialize targets for experiment----
targ_top_right = visual.ShapeStim(
    win=win, name='targ_top_right',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0.3, 0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=0.0, interpolate=True)
targ_mid_right = visual.ShapeStim(
    win=win, name='targ_mid_right',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0.3, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-1.0, interpolate=True)
targ_bot_right = visual.ShapeStim(
    win=win, name='targ_bot_right',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0.3, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-7.0, interpolate=True)
targ_bot_center = visual.ShapeStim(
    win=win, name='targ_bot_center',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-2.0, interpolate=True)
targ_top_center = visual.ShapeStim(
    win=win, name='targ_top_center',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(0, 0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-3.0, interpolate=True)
targ_top_left = visual.ShapeStim(
    win=win, name='targ_top_left',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(-0.3, 0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-4.0, interpolate=True)
targ_mid_left = visual.ShapeStim(
    win=win, name='targ_mid_left',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(-0.3, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-5.0, interpolate=True)
targ_bot_left = visual.ShapeStim(
    win=win, name='targ_bot_left',
    size=(0.2, 0.2), vertices='circle',
    ori=0.0, pos=(-0.3, -0.3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=None, depth=-6.0, interpolate=True)
    
# routine timer to track time remaining of each (possibly non-slip) routine
routineTimer = core.Clock()

#start variables
targ_top_right.status = STARTED
targ_top_right.setAutoDraw(True)
    
targ_mid_right.status = STARTED
targ_mid_right.setAutoDraw(True)
    
targ_bot_right.status = STARTED
targ_bot_right.setAutoDraw(True)
    
targ_bot_center.status = STARTED
targ_bot_center.setAutoDraw(True)
    
targ_top_center.status = STARTED
targ_top_center.setAutoDraw(True)
    
targ_top_left.status = STARTED
targ_top_left.setAutoDraw(True)
    
targ_mid_left.status = STARTED
targ_mid_left.setAutoDraw(True)
    
targ_bot_left.status = STARTED
targ_bot_left.setAutoDraw(True)


        
#have it draw the target
#if targ_top_right.status == STARTED:

