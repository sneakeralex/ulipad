#       Programmer:     limodou
#       E-mail:         limodou@gmail.com
#
#       Copyleft 2006 limodou
#
#       Distributed under the terms of the GPL (GNU Public License)
#
#   UliPad is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#       $Id: mEditor.py 1457 2006-08-23 02:12:12Z limodou $

from modules import Mixin
import wx

def add_panel_list(panellist):
    from TextPanel import TextPanel
    panellist['edit'] = TextPanel
Mixin.setPlugin('editctrl', 'add_panel_list', add_panel_list)

def on_key_down(win, event):
    key = event.KeyCode()
    alt = event.AltDown()
    shift = event.ShiftDown()
    ctrl = event.ControlDown()
    if ctrl and key == wx.WXK_TAB:
        if not shift:
            win.editctrl.forward()
        else:
            win.editctrl.backward()
Mixin.setPlugin('editor', 'on_key_down', on_key_down)
