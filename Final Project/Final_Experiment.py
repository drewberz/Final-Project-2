#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on Tue Apr 30 20:13:19 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
############################################################################
from psychopy import event, logging
from psychopy.visual.shape import ShapeStim
from psychopy.visual.basevisual import MinimalStim

__author__ = 'David Bridges'

from psychopy.tools.attributetools import attributeSetter

#Training Trial Brush
class Brush(MinimalStim): #From brush GitHub documentation, added as a class 
    #instead of importing so we could manipulate its coordinates directly. 
    """A class for creating a freehand drawing tool.

    """
    def __init__(self,
                 win,
                 lineWidth=1.5,
                 lineColor=(1.0, 1.0, 1.0),
                 lineColorSpace='rgb',
                 opacity=1.0,
                 closeShape=False,
                 buttonRequired=True,
                 name=None,
                 depth=0,
                 autoLog=True,
                 autoDraw=False
                 ):

        super(Brush, self).__init__(name=name,
                                    autoLog=False)

        self.win = win
        self.name = name
        self.depth = depth
        self.lineColor = lineColor
        self.lineColorSpace = lineColorSpace
        self.lineWidth = lineWidth
        self.opacity = opacity
        self.closeShape = closeShape
        self.buttonRequired = buttonRequired
        self.pointer = event.Mouse(win=self.win)
        self.shapes = []
        self.brushPos = []
        self.strokeIndex = -1
        self.atStartPoint = False

        self.autoLog = autoLog
        self.autoDraw = autoDraw

        if self.autoLog:
            logging.exp("Created {name} = {obj}".format(name=self.name,
                                                        obj=str(self)))

    def _resetVertices(self):
        """
        Resets list of vertices passed to ShapeStim.
        """
        if self.autoLog:
            logging.exp("Resetting {name} parameter: brushPos.".format(name=self.name))
        self.brushPos = []

    def _createStroke(self):
        """
        Creates ShapeStim for each stroke.
        """
        if self.autoLog:
            logging.exp("Creating ShapeStim for {name}".format(name=self.name))

        self.shapes.append(ShapeStim(self.win,
                                     vertices=[[0, 0]],
                                     closeShape=self.closeShape,
                                     lineWidth=self.lineWidth,
                                     lineColor=self.lineColor,
                                     colorSpace=self.lineColorSpace,
                                     opacity=self.opacity,
                                     autoLog=False,
                                     autoDraw=True))

    @property
    def currentShape(self):
        """The index of current shape to be drawn.

        Returns
        -------
        Int
            The index as length of shapes attribute - 1.
        """
        return len(self.shapes) - 1

    @property
    def brushDown(self):
        """
        Checks whether the mouse button has been clicked in order to start drawing.

        Returns
        -------
        Bool
            True if left mouse button is pressed or if no button press is required, otherwise False.
        """
        if self.buttonRequired:
            return self.pointer.getPressed()[0] == 1
        else:
            return True

    def onBrushDown(self):
        """
        On first brush stroke, empty pointer position list, and create a new ShapeStim.
        """
        if self.brushDown and not self.atStartPoint:
            self.atStartPoint = True
            self._resetVertices()
            self._createStroke()
    
    def onBrushDrag(self):
        """
        Check whether the brush is down. If brushDown is True, the brush path is drawn on screen.
        """
        if self.brushDown:
            self.brushPos.append(self.pointer.getPos())
            self.shapes[self.currentShape].setVertices(self.brushPos)
        else:
            self.atStartPoint = False
        

    def draw(self):
        """
        Get starting stroke and begin painting on screen.
        """
        self.onBrushDown()
        self.onBrushDrag()

    def reset(self):
        """
        Clear ShapeStim objects from shapes attribute.
        """
        if self.autoLog:
            logging.exp("Resetting {name}".format(name=self.name))

        if len(self.shapes):
            for shape in self.shapes:
                shape.setAutoDraw(False)
        self.atStartPoint = False
        self.shapes = []

    @attributeSetter
    def autoDraw(self, value):
        # Do base setting
        MinimalStim.autoDraw.func(self, value)
        # Set autodraw on shapes
        for shape in self.shapes:
            shape.setAutoDraw(value)

    def setLineColor(self, value):
        """
        Sets the line color passed to ShapeStim.

        Parameters
        ----------
        value
            Line color
        """
        self.lineColor = value

    def setLineWidth(self, value):
        """
        Sets the line width passed to ShapeStim.

        Parameters
        ----------
        value
            Line width in pixels
        """
        self.lineWidth = value

    def setOpacity(self, value):
        """
        Sets the line opacity passed to ShapeStim.

        Parameters
        ----------
        value
            Opacity range(0, 1)
        """
        self.opacity = value

    def setButtonRequired(self, value):
        """
        Sets whether or not a button press is needed to draw the line..

        Parameters
        ----------
        value
            Button press required (True or False).
        """
        self.buttonRequired = value
        
        
#Experimental Trial Brush
class Brush2(MinimalStim): #created new brush class with manipulated drawing
    #coordinates to use in the experimental trials
    """A class for creating a freehand drawing tool.

    """
    def __init__(self,
                 win,
                 lineWidth=1.5,
                 lineColor=(1.0, 1.0, 1.0),
                 lineColorSpace='rgb',
                 opacity=1.0,
                 closeShape=False,
                 buttonRequired=True,
                 name=None,
                 depth=0,
                 autoLog=True,
                 autoDraw=False
                 ):

        super(Brush2, self).__init__(name=name,
                                    autoLog=False)

        self.win = win
        self.name = name
        self.depth = depth
        self.lineColor = lineColor
        self.lineColorSpace = lineColorSpace
        self.lineWidth = lineWidth
        self.opacity = opacity
        self.closeShape = closeShape
        self.buttonRequired = buttonRequired
        self.pointer = event.Mouse(win=self.win)
        self.shapes = []
        self.brushPos = []
        self.strokeIndex = -1
        self.atStartPoint = False

        self.autoLog = autoLog
        self.autoDraw = autoDraw

        if self.autoLog:
            logging.exp("Created {name} = {obj}".format(name=self.name,
                                                        obj=str(self)))

    def _resetVertices(self):
        """
        Resets list of vertices passed to ShapeStim.
        """
        if self.autoLog:
            logging.exp("Resetting {name} parameter: brushPos.".format(name=self.name))
        self.brushPos = []

    def _createStroke(self):
        """
        Creates ShapeStim for each stroke.
        """
        if self.autoLog:
            logging.exp("Creating ShapeStim for {name}".format(name=self.name))

        self.shapes.append(ShapeStim(self.win,
                                     vertices=[[0, 0]],
                                     closeShape=self.closeShape,
                                     lineWidth=self.lineWidth,
                                     lineColor=self.lineColor,
                                     colorSpace=self.lineColorSpace,
                                     opacity=self.opacity,
                                     autoLog=False,
                                     autoDraw=True))

    @property
    def currentShape(self):
        """The index of current shape to be drawn.

        Returns
        -------
        Int
            The index as length of shapes attribute - 1.
        """
        return len(self.shapes) - 1

    @property
    def brushDown(self):
        """
        Checks whether the mouse button has been clicked in order to start drawing.

        Returns
        -------
        Bool
            True if left mouse button is pressed or if no button press is required, otherwise False.
        """
        if self.buttonRequired:
            return self.pointer.getPressed()[0] == 1
        else:
            return True

    def onBrushDown(self):
        """
        On first brush stroke, empty pointer position list, and create a new ShapeStim.
        """
        if self.brushDown and not self.atStartPoint:
            self.atStartPoint = True
            self._resetVertices()
            self._createStroke()
    
    def onBrushDrag(self):
        """
        Check whether the brush is down. If brushDown is True, the brush path is drawn on screen.
        """
        
        if self.brushDown:
            self.brushPos.append(self.pointer.getPos() + [0.05, 0.05])
            self.shapes[self.currentShape].setVertices(self.brushPos)
        else:
            self.atStartPoint = False
       

    def draw(self):
        """
        Get starting stroke and begin painting on screen.
        """
        self.onBrushDown()
        self.onBrushDrag()

    def reset(self):
        """
        Clear ShapeStim objects from shapes attribute.
        """
        if self.autoLog:
            logging.exp("Resetting {name}".format(name=self.name))

        if len(self.shapes):
            for shape in self.shapes:
                shape.setAutoDraw(False)
        self.atStartPoint = False
        self.shapes = []

    @attributeSetter
    def autoDraw(self, value):
        # Do base setting
        MinimalStim.autoDraw.func(self, value)
        # Set autodraw on shapes
        for shape in self.shapes:
            shape.setAutoDraw(value)

    def setLineColor(self, value):
        """
        Sets the line color passed to ShapeStim.

        Parameters
        ----------
        value
            Line color
        """
        self.lineColor = value

    def setLineWidth(self, value):
        """
        Sets the line width passed to ShapeStim.

        Parameters
        ----------
        value
            Line width in pixels
        """
        self.lineWidth = value

    def setOpacity(self, value):
        """
        Sets the line opacity passed to ShapeStim.

        Parameters
        ----------
        value
            Opacity range(0, 1)
        """
        self.opacity = value

    def setButtonRequired(self, value):
        """
        Sets whether or not a button press is needed to draw the line..

        Parameters
        ----------
        value
            Button press required (True or False).
        """
        self.buttonRequired = value
############################################################################

# --- Import packages ---
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

import random as pyrandom

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.1'
expName = 'untitled'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/brynnkroke/untitled.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruct" ---
    ########################################################################
    ########################################################################
    instructions = visual.TextBox2(win, text = 'INSTRUCTIONS\nPRESS ANY KEY TO CONTINUE')
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    # --- Initialize components for Routine "Training_Trial" ---
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
        
    #creating list of targets - written by Andrew
    target_list = [targ_top_right, targ_mid_right, targ_bot_right, targ_bot_center, 
    targ_top_center, targ_top_left, targ_mid_left, targ_bot_left]
    #iterate through list randomly
    #target_displayed = pyrandom.choice(target_list)
    test = visual.TextBox2(win, text = 'next routine')
    crosshairs_x = visual.shape.ShapeStim(
    win, units='', colorSpace='rgb', fillColor=False, 
    lineColor=([1, 1, 1]), lineWidth=3.5, vertices=((-0.05, 0), (0.05, 0)), 
    windingRule=None, closeShape=False, pos=(0, 0), size=1, anchor=None, 
    ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, 
    draggable=False, name=None, autoLog=None, autoDraw=False, color=False, 
    lineRGB=False, fillRGB=False, fillColorSpace=None, lineColorSpace=None)
    
    crosshairs_y = visual.shape.ShapeStim(
    win, units='', colorSpace='rgb', fillColor=False, 
    lineColor=([1, 1, 1]), lineWidth=3.5, vertices=((0, -0.05), (0, 0.05)), 
    windingRule=None, closeShape=False, pos=(0, 0), size=1, anchor=None, 
    ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True, 
    draggable=False, name=None, autoLog=None, autoDraw=False, color=False, 
    lineRGB=False, fillRGB=False, fillColorSpace=None, lineColorSpace=None)
    
    crosshairs_dot = visual.shape.ShapeStim(win,
        size=(0.003, 0.003), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-6.0, interpolate=True)
    
    crosshairs_dot2 = visual.shape.ShapeStim(win,
        size=(0.003, 0.003), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
        opacity=None, depth=-6.0, interpolate=True)
        
    brush = Brush(win, lineWidth=3, lineColor=[1, 1, 1,])
    
    targets = [0]
    
    test = visual.TextBox2(win, text = 'next routine')
    
    mouse = event.Mouse()
    ########################################################################
    ########################################################################
    # --- Initialize components for Routine "Shape_Trial" ---
    ##Initialize text to tell participant to do a single motion if they are taking too long to draw line
    too_long = visual.TextBox2(win, text = 'Perform a single, fast motion from the center to the target', pos = (0, -0.15))
    brush2 = Brush2(win, lineWidth=3, lineColor=[1, 1, 1,])
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Instruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruct.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    InstructComponents = [instructions, key_resp]
    for thisComponent in InstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        ####################################################################
        ####################################################################
        if instructions.status == NOT_STARTED:
            instructions.status = STARTED
            instructions.setAutoDraw(True)
        
        if instructions.status == STARTED:
            pass
        
        if key_resp.status == NOT_STARTED:
            key_resp.status = STARTED
        
        if key_resp.status == STARTED:
            keypress = key_resp.getKeys(keyList=None, ignoreKeys = ['escape'])
            if len(keypress) > 0:
                continueRoutine = False
        ####################################################################
        ####################################################################
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruct" ---
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruct.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        #iterate through list randomly
        ##########################################################
        target_displayed = pyrandom.choice(target_list)
        if target_displayed == targets[-1]:
            print('same')
            target_displayed = pyrandom.choice(target_list)
        targets.append(target_displayed)
        ##########################################################
        # --- Prepare to start Routine "Training_Trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Training_Trial.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        Training_TrialComponents = [crosshairs_x, crosshairs_y, crosshairs_dot, brush, target_displayed]
        for thisComponent in Training_TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        clicked = False
        # --- Run Routine "Training_Trial" ---
        routineForceEnded = not continueRoutine
        ######## Initialize brushTimer ###########
        brushTimer = core.Clock()
        brushTimeDiff = 2.5
        start_time = brushTimer.getTime()
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            ####################################################################
            ####################################################################
            
            if crosshairs_x.status == NOT_STARTED:
                crosshairs_x.status == STARTED
                crosshairs_x.setAutoDraw(True)
        
            if crosshairs_y.status == NOT_STARTED:
                crosshairs_y.status == STARTED
                crosshairs_y.setAutoDraw(True)
        
            if crosshairs_dot.status == NOT_STARTED:
                crosshairs_dot.status == STARTED
                crosshairs_dot.setAutoDraw(True)
            
            if target_displayed.status == NOT_STARTED: 
                target_displayed.status == STARTED
                target_displayed.setAutoDraw(True)
        
            if brush.status == NOT_STARTED:
                brush.status = STARTED
            
            if brush.status == STARTED:
                brush.setAutoDraw(True)
                if mouse.getPressed()[0] == 1:
                    clicked = True
                if clicked == True and mouse.getPressed()[0] == 0:
                    brush.status = FINISHED
                    print('finished')
                    if brushTimer.getTime() - start_time > brushTimeDiff:
                        print('too long')
                        brushTimer.reset()
                        if too_long.status == NOT_STARTED:
                            too_long.status = STARTED
                            too_long.setAutoDraw(True)
                        brush.reset()
                        continueRoutine = False #changed from False to True ###not working when True
                    else:
                        print('fast enough')
                        brushTimer.reset()
                        win.flip()
                        brush.reset()
                        continueRoutine = False
                   # elif brushTimer.getTime() < brushTimeDiff:
                        #brush.status = FINISHED
                       # print('not good')
                       # print('took too long')
                       # print(brushTimer.getTime())
                      #  brushTimer.reset()
                      #  win.flip()
                      #  continueRoutine = False
            
        ####################################################################
        ####################################################################
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Training_TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Training_Trial" ---
        for thisComponent in Training_TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Training_Trial.stopped', globalClock.getTime(format='float'))
        # the Routine "Training_Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "Shape_Trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Shape_Trial.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        #Shape_TrialComponents = [crosshairs_x, crosshairs_y, crosshairs_dot, brush2, target_displayed]
        Shape_TrialComponents = [test]
        for thisComponent in Shape_TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Shape_Trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            ###################################################################
            ####################################################################
            
            print("in the while loop")
            
            if test.status == NOT_STARTED:
                test.status = STARTED
            if test.status == STARTED:
                test.setAutoDraw(True)
            #if crosshairs_x.status == NOT_STARTED:
                #crosshairs_x.status == STARTED
                #crosshairs_x.setAutoDraw(True)
        
            #if crosshairs_y.status == NOT_STARTED:
                #crosshairs_y.status == STARTED
                #crosshairs_y.setAutoDraw(True)
        
            #if crosshairs_dot.status == NOT_STARTED:
                #crosshairs_dot.status == STARTED
                #crosshairs_dot.setAutoDraw(True)
            
            #if target_displayed.status == NOT_STARTED: 
                #target_displayed.status == STARTED
                #target_displayed.setAutoDraw(True)
        
            if brush2.status == NOT_STARTED:
                brush2.status = STARTED
        
            if brush2.status == STARTED:
                brush2.setAutoDraw(True)
                if mouse.getPressed()[0] == 1:
                    clicked = True
                if clicked == True and mouse.getPressed()[0] == 0:
                    brush2.status == FINISHED
                    continueRoutine = False
            
        ####################################################################
        ####################################################################
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Shape_TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Shape_Trial" ---
        for thisComponent in Shape_TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Shape_Trial.stopped', globalClock.getTime(format='float'))
        # the Routine "Shape_Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials_2'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
