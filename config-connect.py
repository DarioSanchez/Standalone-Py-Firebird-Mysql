#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import kinterbasdb
import os
import sys
import MySQLdb
import datetime
import time
from os.path import exists
import time
from threading import Timer
import shutil
import string
import wx.xrc
import wx.calendar

# from archivo import *




fecha_hoy = time.strftime(r"%Y-%m-%d %H:%M:%S", time.localtime())
fecha_hoy_Connect1 = time.strftime(r"%m/%d/%Y", time.localtime())
t0 = time.clock()


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Software Project-Connect - Configuracion",
                          pos=wx.DefaultPosition, size=wx.Size(1258, 355),
                          style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(10, 74, 90, 90, False, "Candara"))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.SetBackgroundColour(wx.Colour(211, 211, 211))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Project-Connect\\config\\exe.win32-2.7\\ico.png", wx.BITMAP_TYPE_ANY))

        self.SetIcon(_icon)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY), wx.HORIZONTAL)

        self.m_button3 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Conectar", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.m_button3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button3.SetBackgroundColour(wx.Colour(0, 128, 128))
        sbSizer4.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Enviar Project-Connect al inicio de Windows",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button4.SetBackgroundColour(wx.Colour(0, 128, 128))
        sbSizer4.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Iniciar Project-Connect", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.m_button5.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button5.SetBackgroundColour(wx.Colour(0, 128, 128))
        sbSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Borrar conexion", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.m_button2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button2.SetBackgroundColour(wx.Colour(217, 0, 0))
        sbSizer4.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button65 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Cerrar Proceso CRM", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.m_button65.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button65.SetBackgroundColour(wx.Colour(0, 128, 128))
        sbSizer4.Add(self.m_button65, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button6.SetBackgroundColour(wx.Colour(0, 128, 128))
        sbSizer4.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_staticText167 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u" || Frecuencia de ejecución",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText167.Wrap(-1)
        sbSizer4.Add(self.m_staticText167, 0, wx.ALL, 5)

        if exists("Connect1.txt") == True and exists("Connect2.txt") == True and exists("Connect3.txt") == True:
            archivo = open('Connect1.txt', "r")
            lin_Connect1_fech = list(archivo)

            self.m_textCtrl24 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, lin_Connect1_fech[6],
                                            wx.DefaultPosition, wx.Size(50, -1), 0)
            self.m_textCtrl24.SetBackgroundColour(wx.Colour(255, 224, 193))

            self.m_staticText223 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"(Segundos)", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.m_staticText223.Wrap(-1)
            sbSizer4.Add(self.m_staticText223, 0, wx.ALL, 5)

            sbSizer4.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        elif exists("Connect1.txt") == True and exists("Connect2.txt") == True:
            archivo = open('Connect1.txt', "r")
            lin_Connect1_fech = list(archivo)

            self.m_textCtrl24 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, lin_Connect1_fech[6],
                                            wx.DefaultPosition, wx.Size(50, -1), 0)
            self.m_textCtrl24.SetBackgroundColour(wx.Colour(255, 224, 193))

            self.m_staticText223 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"(Segundos)", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.m_staticText223.Wrap(-1)
            sbSizer4.Add(self.m_staticText223, 0, wx.ALL, 5)

            sbSizer4.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        elif exists("Connect1.txt") == True and exists("Connect3.txt") == True:
            archivo = open('Connect1.txt', "r")
            lin_Connect1_fech = list(archivo)

            self.m_textCtrl24 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, lin_Connect1_fech[6],
                                            wx.DefaultPosition, wx.Size(50, -1), 0)
            self.m_textCtrl24.SetBackgroundColour(wx.Colour(255, 224, 193))

            self.m_staticText223 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"(Segundos)", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.m_staticText223.Wrap(-1)
            sbSizer4.Add(self.m_staticText223, 0, wx.ALL, 5)

            sbSizer4.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        elif exists("Connect2.txt") == True and exists("Connect3.txt") == True:
            archivo = open('Connect2.txt', "r")
            lin_Connect1_fech2 = list(archivo)

            self.m_textCtrl24 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, lin_Connect1_fech2[6],
                                            wx.DefaultPosition, wx.Size(50, -1), 0)
            self.m_textCtrl24.SetBackgroundColour(wx.Colour(255, 224, 193))

            self.m_staticText223 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"(Segundos)", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.m_staticText223.Wrap(-1)
            sbSizer4.Add(self.m_staticText223, 0, wx.ALL, 5)

            sbSizer4.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        else:

            self.m_textCtrl24 = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), 0)
            self.m_textCtrl24.SetBackgroundColour(wx.Colour(255, 224, 193))

            self.m_staticText223 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"(Segundos)", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
            self.m_staticText223.Wrap(-1)
            sbSizer4.Add(self.m_staticText223, 0, wx.ALL, 5)

            sbSizer4.Add(self.m_textCtrl24, 0, wx.ALL, 5)

        bSizer1.Add(sbSizer4, 1, wx.ALIGN_BOTTOM | wx.ALL | wx.BOTTOM | wx.EXPAND, 20)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Base de datos 3"), wx.HORIZONTAL)

        # self.m_staticText1 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Agregar ubicacion de base de datos de Connect1", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        # self.m_staticText1.Wrap( -1 )
        # self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        # sbSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )




        if exists("Connect1.txt") == True or exists("Connect2.txt") == True or exists("Connect3.txt") == True:

            if exists("Connect1.txt") == True:
                archivo = open('Connect1.txt', "r")
                lin_Connect1 = list(archivo)
            else:
                lin_Connect1 = [" ", " ", " ", " ", " ", " "]
            if exists("Connect2.txt") == True:
                archivo2 = open('Connect2.txt', "r")
                lin_Connect2 = list(archivo2)
            else:
                lin_Connect2 = [" ", " ", " ", " ", " ", " "]
            if exists("Connect3.txt") == True:
                archivo3 = open('Connect3.txt', "r")
                lin_Connect3 = list(archivo3)
            else:
                lin_Connect3 = [" ", " ", " ", " ", " ", " "]

            # date_closed = str(lin_Connect1[4])
            # lin_Connect1[4] = datetime.strptime(date_closed,'%d/%m/%Y')

            self.m_staticText2e = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_staticText2e.Wrap(-1)
            sbSizer3.Add(self.m_staticText2e, 0, wx.ALL, 5)

            self.m_textCtrl2e = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[0], wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            sbSizer3.Add(self.m_textCtrl2e, 0, wx.ALL, 5)

            self.m_staticText1e = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText1e.Wrap(-1)
            sbSizer3.Add(self.m_staticText1e, 0, wx.ALL, 5)

            self.m_filePicker1e = wx.FilePickerCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[1], wx.EmptyString,
                                                    u"Select a file", wx.DefaultPosition, wx.DefaultSize,
                                                    wx.FLP_DEFAULT_STYLE)
            sbSizer3.Add(self.m_filePicker1e, 0, wx.ALL, 5)

            # self.m_textCtrl2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY,lin_Connect1[0], wx.DefaultPosition, wx.DefaultSize, 0 )
            # sbSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

            self.m_staticText2 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText2.Wrap(-1)
            self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

            self.m_textCtrl3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[2], wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

            self.m_staticText3 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText3.Wrap(-1)
            self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
            self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

            self.m_textCtrl1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[3], style=wx.TE_PASSWORD)
            self.m_textCtrl1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
            sbSizer3.Add(self.m_textCtrl1, 0, wx.ALL, 5)

            # DESDE HASTA self.editname = wx.TextCtrl(self, value="", pos=(120, 60), size=(140,-1))

            self.m_staticText9 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Desde", wx.Point(-1, -1),
                                               wx.DefaultSize, 0)
            self.m_staticText9.Wrap(-1)
            sbSizer3.Add(self.m_staticText9, 0, wx.ALL, 5)

            self.m_staticText91 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[4], wx.Point(-1, -1),
                                                wx.DefaultSize, 0)
            self.m_staticText91.Wrap(-1)
            self.m_staticText91.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText91.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizer3.Add(self.m_staticText91, 0, wx.ALL, 5)

            self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.Point(-1, -1),
                                                wx.DefaultSize, 0)
            self.m_staticText10.Wrap(-1)
            sbSizer3.Add(self.m_staticText10, 0, wx.ALL, 5)

            self.m_staticText10x = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, lin_Connect1[5], wx.Point(-1, -1),
                                                 wx.DefaultSize, 0)
            self.m_staticText10x.Wrap(-1)
            self.m_staticText10x.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText10x.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizer3.Add(self.m_staticText10x, 0, wx.ALL, 5)

            # *******************
            sbSizerdb2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Base de datos 1"), wx.HORIZONTAL)

            self.m_staticText1db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText1db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText1db2, 0, wx.ALL, 5)

            self.m_textCtrl2db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[0], wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb2.Add(self.m_textCtrl2db2, 0, wx.ALL, 5)

            self.m_staticText2db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText2db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText2db2, 0, wx.ALL, 5)

            self.m_filePicker1db2 = wx.FilePickerCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[1],
                                                      wx.EmptyString, u"Select a file", wx.DefaultPosition,
                                                      wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
            sbSizerdb2.Add(self.m_filePicker1db2, 0, wx.ALL, 5)

            self.m_staticText3db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText3db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText3db2, 0, wx.ALL, 5)

            self.m_textCtrl4db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[2], wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb2.Add(self.m_textCtrl4db2, 0, wx.ALL, 5)

            self.m_staticText4db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText4db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText4db2, 0, wx.ALL, 5)

            self.m_textCtrl5db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[3],
                                              style=wx.TE_PASSWORD)
            sbSizerdb2.Add(self.m_textCtrl5db2, 0, wx.ALL, 5)

            self.m_staticText5db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Desde", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText5db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText5db2, 0, wx.ALL, 5)

            self.m_staticText5db2c = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[4],
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText5db2c.Wrap(-1)
            self.m_staticText5db2c.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText5db2c.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizerdb2.Add(self.m_staticText5db2c, 0, wx.ALL, 5)

            self.m_staticText6db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText6db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText6db2, 0, wx.ALL, 5)

            self.m_staticText6db2c = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, lin_Connect3[5],
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText6db2c.Wrap(-1)
            self.m_staticText6db2c.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText6db2c.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizerdb2.Add(self.m_staticText6db2c, 0, wx.ALL, 5)

            bSizer1.Add(sbSizerdb2, 1, wx.EXPAND, 5)

            # *********************************************************
            sbSizerdb3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Base de datos 2"), wx.HORIZONTAL)

            self.m_staticText1db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText1db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText1db3, 0, wx.ALL, 5)

            self.m_textCtrl2db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[0], wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb3.Add(self.m_textCtrl2db3, 0, wx.ALL, 5)

            self.m_staticText2db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText2db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText2db3, 0, wx.ALL, 5)

            self.m_filePicker1db3 = wx.FilePickerCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[1],
                                                      wx.EmptyString, u"Select a file", wx.DefaultPosition,
                                                      wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
            sbSizerdb3.Add(self.m_filePicker1db3, 0, wx.ALL, 5)

            self.m_staticText3db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText3db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText3db3, 0, wx.ALL, 5)

            self.m_textCtrl4db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[2], wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb3.Add(self.m_textCtrl4db3, 0, wx.ALL, 5)

            self.m_staticText4db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText4db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText4db3, 0, wx.ALL, 5)

            self.m_textCtrl5db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[3],
                                              style=wx.TE_PASSWORD)
            sbSizerdb3.Add(self.m_textCtrl5db3, 0, wx.ALL, 5)

            self.m_staticText5db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Desde", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText5db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText5db3, 0, wx.ALL, 5)

            self.m_staticText5db3c = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[4],
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText5db3c.Wrap(-1)
            self.m_staticText5db3c.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText5db3c.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizerdb3.Add(self.m_staticText5db3c, 0, wx.ALL, 5)

            self.m_staticText6db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText6db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText6db3, 0, wx.ALL, 5)

            self.m_staticText6db3c = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, lin_Connect2[5],
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText6db3c.Wrap(-1)
            self.m_staticText6db3c.SetFont(wx.Font(10, 74, 90, 90, False))
            self.m_staticText6db3c.SetForegroundColour(wx.Colour(0, 122, 244))
            sbSizerdb3.Add(self.m_staticText6db3c, 0, wx.ALL, 5)

            bSizer1.Add(sbSizerdb3, 1, wx.EXPAND, 5)














        else:

            # **************************

            self.m_staticText2e = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_staticText2e.Wrap(-1)
            sbSizer3.Add(self.m_staticText2e, 0, wx.ALL, 5)

            self.m_textCtrl2e = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            sbSizer3.Add(self.m_textCtrl2e, 0, wx.ALL, 5)

            self.m_staticText1e = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText1e.Wrap(-1)
            sbSizer3.Add(self.m_staticText1e, 0, wx.ALL, 5)

            self.m_filePicker1e = wx.FilePickerCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"", u"Selecciona un db",
                                                    wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    wx.FLP_DEFAULT_STYLE)
            sbSizer3.Add(self.m_filePicker1e, 0, wx.ALL, 5)

            # self.m_textCtrl2 = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY,lin_Connect1[0], wx.DefaultPosition, wx.DefaultSize, 0 )
            # sbSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

            self.m_staticText2 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText2.Wrap(-1)
            self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

            self.m_textCtrl3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

            self.m_staticText3 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText3.Wrap(-1)
            self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
            self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

            self.m_textCtrl1 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, style=wx.TE_PASSWORD)
            self.m_textCtrl1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
            sbSizer3.Add(self.m_textCtrl1, 0, wx.ALL, 5)

            # DESDE HASTA self.editname = wx.TextCtrl(self, value="", pos=(120, 60), size=(140,-1))

            self.m_staticText9 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Desde", wx.Point(-1, -1),
                                               wx.DefaultSize, 0)
            self.m_staticText9.Wrap(-1)
            sbSizer3.Add(self.m_staticText9, 0, wx.ALL, 5)

            self.m_datePicker1 = wx.DatePickerCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizer3.Add(self.m_datePicker1, 0, wx.ALL, 5)

            self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.Point(-1, -1),
                                                wx.DefaultSize, 0)
            self.m_staticText10.Wrap(-1)
            sbSizer3.Add(self.m_staticText10, 0, wx.ALL, 5)

            self.m_datePicker2 = wx.DatePickerCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizer3.Add(self.m_datePicker2, 0, wx.ALL, 5)

            # *******************
            # *******************
            sbSizerdb2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Base de datos 1"), wx.HORIZONTAL)

            self.m_staticText1db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText1db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText1db2, 0, wx.ALL, 5)

            self.m_textCtrl2db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb2.Add(self.m_textCtrl2db2, 0, wx.ALL, 5)

            self.m_staticText2db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText2db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText2db2, 0, wx.ALL, 5)

            self.m_filePicker1db2 = wx.FilePickerCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                      u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                      wx.FLP_DEFAULT_STYLE)
            sbSizerdb2.Add(self.m_filePicker1db2, 0, wx.ALL, 5)

            self.m_staticText3db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText3db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText3db2, 0, wx.ALL, 5)

            self.m_textCtrl4db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb2.Add(self.m_textCtrl4db2, 0, wx.ALL, 5)

            self.m_staticText4db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText4db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText4db2, 0, wx.ALL, 5)

            self.m_textCtrl5db2 = wx.TextCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb2.Add(self.m_textCtrl5db2, 0, wx.ALL, 5)

            self.m_staticText5db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Desde", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText5db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText5db2, 0, wx.ALL, 5)

            self.m_datePicker1db2 = wx.DatePickerCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizerdb2.Add(self.m_datePicker1db2, 0, wx.ALL, 5)

            self.m_staticText6db2 = wx.StaticText(sbSizerdb2.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText6db2.Wrap(-1)
            sbSizerdb2.Add(self.m_staticText6db2, 0, wx.ALL, 5)

            self.m_datePicker2db2 = wx.DatePickerCtrl(sbSizerdb2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizerdb2.Add(self.m_datePicker2db2, 0, wx.ALL, 5)

            bSizer1.Add(sbSizerdb2, 1, wx.EXPAND, 5)

            # *********************************************************
            sbSizerdb3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Base de datos 2"), wx.HORIZONTAL)

            self.m_staticText1db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Host", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText1db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText1db3, 0, wx.ALL, 5)

            self.m_textCtrl2db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb3.Add(self.m_textCtrl2db3, 0, wx.ALL, 5)

            self.m_staticText2db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Ubicacion de base de datos",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
            self.m_staticText2db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText2db3, 0, wx.ALL, 5)

            self.m_filePicker1db3 = wx.FilePickerCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                      u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                      wx.FLP_DEFAULT_STYLE)
            sbSizerdb3.Add(self.m_filePicker1db3, 0, wx.ALL, 5)

            self.m_staticText3db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText3db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText3db3, 0, wx.ALL, 5)

            self.m_textCtrl4db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb3.Add(self.m_textCtrl4db3, 0, wx.ALL, 5)

            self.m_staticText4db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText4db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText4db3, 0, wx.ALL, 5)

            self.m_textCtrl5db3 = wx.TextCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
            sbSizerdb3.Add(self.m_textCtrl5db3, 0, wx.ALL, 5)

            self.m_staticText5db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Desde", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText5db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText5db3, 0, wx.ALL, 5)

            self.m_datePicker1db3 = wx.DatePickerCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizerdb3.Add(self.m_datePicker1db3, 0, wx.ALL, 5)

            self.m_staticText6db3 = wx.StaticText(sbSizerdb3.GetStaticBox(), wx.ID_ANY, u"Hasta", wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
            self.m_staticText6db3.Wrap(-1)
            sbSizerdb3.Add(self.m_staticText6db3, 0, wx.ALL, 5)

            self.m_datePicker2db3 = wx.DatePickerCtrl(sbSizerdb3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT)
            sbSizerdb3.Add(self.m_datePicker2db3, 0, wx.ALL, 5)

            bSizer1.Add(sbSizerdb3, 1, wx.EXPAND, 5)

        bSizer1.Add(sbSizer3, 1, wx.EXPAND | wx.ALL, 5)

        # base de datos 2



        # base de datos 3

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"DATOS DE Project-Connect"), wx.HORIZONTAL)

        if exists("line.txt") == True:

            archivo_line = open('line.txt', "r")
            lin_line = list(archivo_line)
            archivo_line.seek(0)
            self.m_staticText6 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Host:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText6.Wrap(-1)
            self.m_staticText6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText6, 0, wx.ALL, 5)

            self.m_textCtrl6 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, lin_line[0], wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl6, 0, wx.ALL, 5)

            self.m_staticText7 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText7.Wrap(-1)
            self.m_staticText7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText7, 0, wx.ALL, 5)

            self.m_textCtrl7 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, lin_line[1], wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl7, 0, wx.ALL, 5)

            self.m_staticText8 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Passowrd", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText8.Wrap(-1)
            self.m_staticText8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText8, 0, wx.ALL, 5)

            self.m_textCtrl8 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, lin_line[2], style=wx.TE_PASSWORD)
            sbSizer2.Add(self.m_textCtrl8, 0, wx.ALL, 5)

            self.m_staticText10 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Puerto ", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_staticText10.Wrap(-1)
            self.m_staticText10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText10, 0, wx.ALL, 5)

            self.m_textCtrl9 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, lin_line[3], wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl9, 0, wx.ALL, 5)
        else:
            self.m_staticText6 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Host:", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText6.Wrap(-1)
            self.m_staticText6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText6, 0, wx.ALL, 5)

            self.m_textCtrl6 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl6, 0, wx.ALL, 5)

            self.m_staticText7 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Usuario", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText7.Wrap(-1)
            self.m_staticText7.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText7, 0, wx.ALL, 5)

            self.m_textCtrl7 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl7, 0, wx.ALL, 5)

            self.m_staticText8 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Passowrd", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
            self.m_staticText8.Wrap(-1)

            self.m_staticText8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText8, 0, wx.ALL, 5)

            self.m_textCtrl8 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl8, 0, wx.ALL, 5)

            self.m_staticText10 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"Puerto ", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
            self.m_staticText10.Wrap(-1)
            self.m_staticText10.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

            sbSizer2.Add(self.m_staticText10, 0, wx.ALL, 5)

            self.m_textCtrl9 = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
            sbSizer2.Add(self.m_textCtrl9, 0, wx.ALL, 5)

        bSizer1.Add(sbSizer2, 1, wx.EXPAND | wx.ALL, 5)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"STATUS DE CONEXION A Connect1"), wx.VERTICAL)

        self.m_staticText101 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)
        # self.m_staticText101.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )



        sbSizer4.Add(self.m_staticText101, 0, wx.ALL, 5)

        self.m_staticText102 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText102.Wrap(-1)
        # self.m_staticText101.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )



        sbSizer4.Add(self.m_staticText102, 0, wx.ALL, 5)

        self.m_staticText102b = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText102b.Wrap(-1)
        # self.m_staticText101.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )



        sbSizer4.Add(self.m_staticText102b, 0, wx.ALL, 5)

        self.m_staticText109 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText109.Wrap(-1)
        # self.m_staticText101.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )



        sbSizer4.Add(self.m_staticText109, 0, wx.ALL, 5)

        self.m_staticText111 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)
        # self.m_staticText11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        sbSizer4.Add(self.m_staticText111, 0, wx.ALL, 5)

        bSizer1.Add(sbSizer4, 1, wx.EXPAND | wx.ALL, 5)

        sbSizer31 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_staticText81 = wx.StaticText(sbSizer31.GetStaticBox(), wx.ID_ANY, u"Software Project-Connect",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        self.m_staticText81.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        sbSizer31.Add(self.m_staticText81, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        # self.m_bitmap1 = wx.StaticBitmap( sbSizer31.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"C:\\Project-Connect\\config\\exe.win32-2.7\\ico.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition,wx.Size( 50,50 ),0 )
        # self.m_bitmap1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

        # sbSizer31.Add( self.m_bitmap1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        bSizer1.Add(sbSizer31, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu2 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"SALIR", wx.EmptyString, wx.ITEM_NORMAL)
        salirf = self.m_menu2.AppendItem(self.m_menuItem1)

        self.Bind(wx.EVT_MENU, self.salir, salirf)

        self.m_menubar2.Append(self.m_menu2, u"SALIR DE Project-Connect")

        self.SetMenuBar(self.m_menubar2)

        self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.m_statusBar1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_statusBar1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        self.Centre(wx.BOTH)

        self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        bSizer1.Add(self.m_gauge1, 0, wx.ALL | wx.EXPAND, 5)
        self.m_gauge1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.evento_cancel)
        self.m_button3.Bind(wx.EVT_BUTTON, self.evento_ok)
        self.m_button2.Bind(wx.EVT_BUTTON, self.reset_con)
        self.m_button4.Bind(wx.EVT_BUTTON, self.iniwindows)
        self.m_button5.Bind(wx.EVT_BUTTON, self.ejex)
        self.m_button65.Bind(wx.EVT_BUTTON, self.stop_process)

    def __del__(self):
        pass

    def salir(self, event):
        self.Close(True)

    # Virtual event handlers, overide them in your derived class
    def evento_cancel(self, event):
        os.startfile(r"C:\Project-Connect\preset\stopcrmui.bat")
        self.Close(True)

    def reset_con(self, event):

        if exists("Connect1.txt") == True:
            os.remove('Connect1.txt')
        else:
            Connect1_reset = "No se encuentra archivo!!"
        if exists("Connect2.txt") == True:
            os.remove('Connect2.txt')
        else:
            Connect1_reset2 = "No se encuentra archivo!!"
        if exists("Connect3.txt") == True:
            os.remove('Connect3.txt')
        else:
            Connect1_reset3 = "No se encuentra archivo!!"
        if exists("line.txt") == True:
            os.remove('line.txt')
        else:
            Connect1_reset3 = "No se encuentra archivo!!"

        self.Close(True)
        os.startfile(r"C:\Project-Connect\config\exe.win32-2.7\config_Project-Connect.exe")

    def iniwindows(self, event):
        os.startfile(r"C:\Project-Connect\preset\config.bat")

    def ejex(self, event):
        os.startfile(r"C:\Project-Connect\preset\ejex.bat")

    def stop_process(self, event):
        os.startfile(r"C:\Project-Connect\preset\stop.bat")

    def evento_ok(self, event):
        self.m_gauge1.SetValue(1)

        if exists("Connect1.txt") == True:
            Connect1 = self.m_filePicker1e.GetPath()
            Connect1Host = self.m_textCtrl2e.GetValue()
            Connect1_user = self.m_textCtrl3.GetValue()
            Connect1_pass = self.m_textCtrl1.GetValue()
            desde1 = ""
            hasta1 = ""
        else:

            Connect1 = self.m_filePicker1e.GetPath()
            Connect1Host = self.m_textCtrl2e.GetValue()
            Connect1_user = self.m_textCtrl3.GetValue()
            Connect1_pass = self.m_textCtrl1.GetValue()
            desde1 = self.m_datePicker1.GetValue().Format('%Y/%m/%d').encode()
            hasta1 = self.m_datePicker2.GetValue().Format('%Y/%m/%d').encode()

        if exists("Connect2.txt") == True:
            Connect2 = self.m_filePicker1db3.GetPath()
            Connect1Host2 = self.m_textCtrl2db3.GetValue()
            Connect1_user2 = self.m_textCtrl4db3.GetValue()
            Connect1_pass2 = self.m_textCtrl5db3.GetValue()
            desde2 = ""
            hasta2 = ""
        else:
            Connect2 = self.m_filePicker1db3.GetPath()
            Connect1Host2 = self.m_textCtrl2db3.GetValue()
            Connect1_user2 = self.m_textCtrl4db3.GetValue()
            Connect1_pass2 = self.m_textCtrl5db3.GetValue()
            desde2 = self.m_datePicker1db3.GetValue().Format('%Y/%m/%d').encode()
            hasta2 = self.m_datePicker2db3.GetValue().Format('%Y/%m/%d').encode()
        if exists("Connect3.txt") == True:

            Connect3 = self.m_filePicker1db2.GetPath()
            Connect1Host3 = self.m_textCtrl2db2.GetValue()
            Connect1_user3 = self.m_textCtrl4db2.GetValue()
            Connect1_pass3 = self.m_textCtrl5db2.GetValue()
            desde3 = ""
            hasta3 = ""
        else:
            Connect3 = self.m_filePicker1db2.GetPath()
            Connect1Host3 = self.m_textCtrl2db2.GetValue()
            Connect1_user3 = self.m_textCtrl4db2.GetValue()
            Connect1_pass3 = self.m_textCtrl5db2.GetValue()
            desde3 = self.m_datePicker1db2.GetValue().Format('%Y/%m/%d').encode()
            hasta3 = self.m_datePicker2db2.GetValue().Format('%Y/%m/%d').encode()

        # --------------------------------------#
        db_host_s = self.m_textCtrl6.GetValue()

        usuario_s = self.m_textCtrl7.GetValue()

        clave_s = self.m_textCtrl8.GetValue()

        frec_seg = self.m_textCtrl24.GetValue()

        port_s = self.m_textCtrl9.GetValue()

        self.m_gauge1.SetValue(10)
        # *************base de datos 3

        if exists("Connect1.txt") == True:

            archivo = open('Connect1.txt', 'r+')
            lineas = list(archivo)

            archivo.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect1.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect1.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect1.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)


        else:
            Connect1_ub_txt = Connect1
            Connect1_user_txt = Connect1_user
            Connect1_pass_txt = Connect1_pass
            Connect1Host = Connect1Host
            frec_seg = frec_seg
            desde1 = desde1
            hasta1 = hasta1
            archivo = open('Connect1.txt', 'w')
            archivo.write(Connect1Host + '\n')
            archivo.write(Connect1_ub_txt + '\n')
            archivo.write(Connect1_user_txt + '\n')
            archivo.write(Connect1_pass_txt + '\n')
            archivo.write(desde1 + '\n')
            archivo.write(hasta1 + '\n')
            archivo.write(frec_seg + '\n')
            archivo = open('Connect1.txt', 'r')
            lineas = list(archivo)

            archivo.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect1.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect1.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect1.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)
        # ********************************base de datos 2


        if exists("Connect2.txt") == True:

            archivo2 = open('Connect2.txt', 'r+')
            lineas2 = list(archivo2)

            archivo2.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect2.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect2.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect2.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)


        else:
            Connect1_ub_txt2 = Connect2
            Connect1_user_txt2 = Connect1_user2
            Connect1_pass_txt2 = Connect1_pass2
            Connect1Host2 = Connect1Host2
            desde2 = desde2
            hasta2 = hasta2
            frec_seg = frec_seg
            archivo2 = open('Connect2.txt', 'w')
            archivo2.write(Connect1Host2 + '\n')
            archivo2.write(Connect1_ub_txt2 + '\n')
            archivo2.write(Connect1_user_txt2 + '\n')
            archivo2.write(Connect1_pass_txt2 + '\n')
            archivo2.write(desde2 + '\n')
            archivo2.write(hasta2 + '\n')
            archivo2.write(frec_seg + '\n')
            archivo2 = open('Connect2.txt', 'r')
            lineas2 = list(archivo2)

            archivo2.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect2.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect2.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect2.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)
        # ********************************base de datos 1

        if exists("Connect3.txt") == True:

            archivo3 = open('Connect3.txt', 'r+')
            lineas3 = list(archivo3)

            archivo3.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect3.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect3.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect3.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)


        else:
            Connect1_ub_txt3 = Connect3
            Connect1_user_txt3 = Connect1_user3
            Connect1_pass_txt3 = Connect1_pass3
            Connect1Host3 = Connect1Host3
            desde3 = desde3
            hasta3 = hasta3
            frec_seg = frec_seg
            archivo3 = open('Connect3.txt', 'w')
            archivo3.write(Connect1Host3 + '\n')
            archivo3.write(Connect1_ub_txt3 + '\n')
            archivo3.write(Connect1_user_txt3 + '\n')
            archivo3.write(Connect1_pass_txt3 + '\n')
            archivo3.write(desde3 + '\n')
            archivo3.write(hasta3 + '\n')
            archivo3.write(frec_seg + '\n')
            archivo3 = open('Connect3.txt', 'r')
            lineas3 = list(archivo3)

            archivo3.close
            origen = r'C:\Project-Connect\config\exe.win32-2.7\Connect3.txt'
            destino = r'C:\Project-Connect\build\exe.win32-2.7\Connect3.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino, 'w') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)

            destino2 = r'C:\Project-Connect\preset\Connect3.txt'
            ruta = os.getcwd() + os.sep

            if os.path.exists(origen):
                with open(origen, 'r') as forigen:
                    with open(destino2, 'w') as fdestino2:
                        shutil.copyfileobj(forigen, fdestino2)
        # *******************************************************
        if db_host_s == "" or usuario_s == "" or clave_s == "" or port_s == "":

            line_errorar = ">>> [004text] No debe dejar ningun campo de Project-Connect vacio!!!"



        else:

            if exists("line.txt") == True:

                archivo_line = open('line.txt', 'r+')
                connect_line = list(archivo_line)

                archivo_line.close
                origen = r'C:\Project-Connect\config\exe.win32-2.7\line.txt'

                destino = r'C:\Project-Connect\build\exe.win32-2.7\line.txt'
                ruta = os.getcwd() + os.sep

                if os.path.exists(origen):
                    with open(origen, 'r') as forigen:
                        with open(destino, 'w') as fdestino:
                            shutil.copyfileobj(forigen, fdestino)

                destino2 = r'C:\Project-Connect\preset\line.txt'
                ruta = os.getcwd() + os.sep

                if os.path.exists(origen):
                    with open(origen, 'r') as forigen:
                        with open(destino2, 'w') as fdestino2:
                            shutil.copyfileobj(forigen, fdestino2)
            else:
                line_ub_txt = db_host_s
                line_user_txt = usuario_s
                line_pass_txt = clave_s
                line_port_txt = port_s
                archivo_line = open('line.txt', 'w')
                archivo_line.write(line_ub_txt + '\n')
                archivo_line.write(line_user_txt + '\n')
                archivo_line.write(line_pass_txt + '\n')
                archivo_line.write(line_port_txt)
                archivo_line = open('line.txt', 'r')
                connect_line = list(archivo_line)
                archivo_line.close

                origen = r'C:\Project-Connect\config\exe.win32-2.7\line.txt'
                destino = r'C:\Project-Connect\build\exe.win32-2.7\line.txt'
                ruta = os.getcwd() + os.sep

                if os.path.exists(origen):
                    with open(origen, 'r') as forigen:
                        with open(destino, 'w') as fdestino:
                            shutil.copyfileobj(forigen, fdestino)

                destino2 = r'C:\Project-Connect\preset\line.txt'
                ruta = os.getcwd() + os.sep

                if os.path.exists(origen):
                    with open(origen, 'r') as forigen:
                        with open(destino2, 'w') as fdestino2:
                            shutil.copyfileobj(forigen, fdestino2)

        self.m_gauge1.SetValue(15)

        con = True
        conn = True
        con2 = True
        con3 = True
        conectado1 = 0
        conectado2 = 0
        conectado3 = 0

        try:

            con = kinterbasdb.connect(dsn=lineas[0].strip() + ":" + lineas[1].strip(), user=str(lineas[2].strip()),
                                      password=str(lineas[3].strip()))

            Connect1_susses = ">>>BASE DE DATOS 3 : Conectado!!"
            conectado1 = 1
            font1 = self.m_staticText101.GetFont()
            font1.SetPointSize(9)
            self.m_staticText101.SetFont(font1)
            self.m_staticText101.SetForegroundColour("#21610B")
            self.m_staticText101.SetLabelText(Connect1_susses)


        except:

            Connect1_error = ">>>BASE DE DATOS 3 : Error de conexion..."
            font1 = self.m_staticText101.GetFont()
            font1.SetPointSize(9)
            self.m_staticText101.SetFont(font1)
            self.m_staticText101.SetForegroundColour("#FF0000")
            self.m_staticText101.SetLabelText(Connect1_error)

        try:

            con2 = kinterbasdb.connect(dsn=lineas2[0].strip() + ":" + lineas2[1].strip(), user=str(lineas2[2].strip()),
                                       password=str(lineas2[3].strip()))

            Connect1_susses = ">>>BASE DE DATOS 2 : Conectado!!"
            conectado2 = 1
            font1 = self.m_staticText102.GetFont()
            font1.SetPointSize(9)
            self.m_staticText102.SetFont(font1)
            self.m_staticText102.SetForegroundColour("#21610B")
            self.m_staticText102.SetLabelText(Connect1_susses)


        except:

            Connect1_error = ">>>BASE DE DATOS 2 : Error de conexion..."
            font1 = self.m_staticText102.GetFont()
            font1.SetPointSize(9)
            self.m_staticText102.SetFont(font1)
            self.m_staticText102.SetForegroundColour("#FF0000")
            self.m_staticText102.SetLabelText(Connect1_error)

        try:

            con3 = kinterbasdb.connect(dsn=lineas3[0].strip() + ":" + lineas3[1].strip(), user=str(lineas3[2].strip()),
                                       password=str(lineas3[3].strip()))

            Connect1_susses = ">>>BASE DE DATOS 1 : Conectado!!"
            conectado3 = 1
            font1 = self.m_staticText102b.GetFont()
            font1.SetPointSize(9)
            self.m_staticText102b.SetFont(font1)
            self.m_staticText102b.SetForegroundColour("#21610B")
            self.m_staticText102b.SetLabelText(Connect1_susses)


        except:

            Connect1_error = ">>>BASE DE DATOS 1 : Error de conexion..."
            font1 = self.m_staticText102b.GetFont()
            font1.SetPointSize(9)
            self.m_staticText102b.SetFont(font1)
            self.m_staticText102b.SetForegroundColour("#FF0000")
            self.m_staticText102b.SetLabelText(Connect1_error)

        self.m_gauge1.SetValue(50)
        try:

            db = MySQLdb.connect(host=connect_line[0].strip(), port=int(connect_line[3].strip()),
                                 user=connect_line[1].strip(), passwd=connect_line[2].strip(), db='[NAME_DB_CONNECT]')

            line_susses = ">>>Connect1 CRM : Conectado!!"
            font1 = self.m_staticText111.GetFont()
            font1.SetPointSize(9)
            self.m_staticText111.SetFont(font1)
            self.m_staticText111.SetForegroundColour("#21610B")
            self.m_staticText111.SetLabelText(line_susses)

        except:

            line_error = ">>>Connect1 CRM: Error de conexion..."
            font1 = self.m_staticText111.GetFont()
            font1.SetPointSize(9)
            self.m_staticText111.SetFont(font1)
            self.m_staticText111.SetForegroundColour("#FF0000")
            self.m_staticText111.SetLabelText(line_error)

        self.m_gauge1.SetValue(60)
        fecha_de_hoy = time.strftime("%Y/%m/%d")

        self.m_gauge1.SetValue(76)
        self.m_gauge1.SetValue(80)
        self.m_gauge1.SetValue(90)
        self.m_gauge1.SetValue(100)

        for i in xrange(10000000):
            pass


app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()


