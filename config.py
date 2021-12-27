# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile

from typing import List  # noqa: F401

from libqtile import bar, widget, hook
from libqtile.config import Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings.keys import mod, keys, myTerm
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
# from settings.widgets import widget_defaults, extension_defaults
# from settings.screens import screens
# from settings.path import qtile_path

###Colors###
dt = [["#282c34", "#282c34"], # panel background ----black
          ["#3d3f4b", "#434758"], # background for current screen tab ----gray
          ["#ffffff", "#ffffff"], # font color for group names ----white
          ["#ff5555", "#ff5555"], # border line color for current tab ----pink
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets' ----green
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets' ----purple
          ["#e1acff", "#e1acff"], # window name ----purple/pink
          ["#ecbbfb", "#ecbbfb"]] # background for inactive screens 

blue = [["#282c34", "#282c34"], # 0 panel background ----black
        ["#3d3f4b", "#434758"], # 1 background for current screen tab ----gray
        ["#ffffff", "#ffffff"], # 2 font color for group names ----white
        ["#A230ED", "#A230ED"], # 3 Gradient
        ["#3D388F", "#3D388F"], # 4 Gradient
        ["#2D58BD", "#2D58BD"], # 5 Gradient
        ["#00A5E1", "#00A5E1"], # 6 Gradient
        ["#53D5D7", "#53D5D7"], # 7 Gradient
        ["#37D5D6", "#36096D"]] # 8 blue slide

colors = blue
#'#eee'

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def powerline(back, fore):
    return widget.TextBox(
        text = '',
        background = back,
        foreground = fore,
        padding = -14,
        fontsize = 48
    )
# triangle icon?
#""    ﱣ

def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
        ),
        widget.GroupBox(
            font = "Ubuntu Nerd Font",
            fontsize = 17,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            active = colors[8],
            inactive = dt[2],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            other_current_screen_border = colors[6],
            other_screen_border = colors[4],
            foreground = colors[2],
            background = colors[0]
        ),
        widget.Prompt(
            prompt = prompt,
            font = "Ubuntu Mono",
            padding = 10,
            foreground = colors[3],
            background = colors[1]
        ),
        widget.Sep(
            linewidth = 0,
            padding = 40,
            foreground = colors[2],
            background = colors[0]
        ),
        widget.WindowName(
            fontsize = 14,
            foreground = colors[7],
            background = colors[0],
            padding = 4
        ),
        widget.Systray(
            background = colors[0],
            padding = 5
        ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0]
        ),
        powerline(colors[0], colors[7]),
        # widget.TextBox(
            # text = '\ue0b6',
            # fonts="droid sans mono for powerline",
            # background = colors[0],
            # foreground = colors[7],
            # padding = -14,
            # fontsize = 48
        # ),
        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[0],
            background = colors[7],
            padding = 0,
            scale = 0.7
        ),
        powerline(colors[7], colors[6]),
        widget.TextBox(
            text = "",
            padding = 5,
            foreground = colors[2],
            background = colors[6],
            fontsize = 14
        ),
        widget.Clock(
            foreground = colors[2],
            background = colors[6],
            fontsize = 16,
            format = "%A, %B %d - %H:%M "
        ),
        powerline(colors[6], colors[5]),
        widget.Net(
            interface = "wlo1",
            format = '{down} ↓↑ {up}',
            foreground = colors[2],
            background = colors[5],
            padding = 5
        ),
        powerline(colors[5], colors[4]),
        widget.TextBox(
            text = " ⟳",
            padding = 5,
            foreground = colors[2],
            background = colors[4],
            fontsize = 14
        ),
        widget.CheckUpdates(
            update_interval = 1800,
            distro = "Ubuntu",
            display_format = "{updates} Updates",
            foreground = colors[2],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo apt update; sudo apt upgrade')},
            background = colors[4]
        ),
        powerline(colors[4], colors[7]),
        widget.TextBox(
            text = " ",
            foreground = colors[2],
            background = colors[7],
            padding = 0,
            fontsize = 17
        ),
        widget.Memory(
            foreground = colors[2],
            background = colors[7],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            padding = 5,
        ),
        powerline(colors[7], colors[6]),
        widget.TextBox(
            text = "墳",
            foreground = colors[2],
            background = colors[6],
            padding = 0
        ),
        widget.Volume(
            foreground = colors[2],
            background = colors[6],
            padding = 5
        ),
        powerline(colors[6], colors[5]),
        widget.TextBox(
            text = "",
            foreground = colors[2],
            background = colors[5],
            padding = 0
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            brightness_file="brightness",
            change_command="brightnessctl -set {0}",
            background = colors[5],
            foreground = colors[2],
            padding = 5,
        ),
        powerline(colors[5], colors[4]),
        widget.BatteryIcon(
            background= colors[4],
            update_interval=60,
            padding = 0,
        ),
        widget.Battery(
            format="{percent:2.0%}",
            background = colors[4],
            foreground = colors[2],
            padding = 5,
        ),
        powerline(colors[4], colors[3]),
        widget.QuickExit(
            default_text = '⏻',
            foreground = colors[2],
            background = colors[3],
            padding =5,
        ),
    ]
    return widgets_list

#拉襤⏻

def init_widgets_screen():
    widgets_screen = init_widgets_list()
    return widgets_screen                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=0.8, size=22, margin=3)),
        Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=0.8, size=24, margin=3)),
    ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen = init_widgets_screen()

"""
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)
"""

# Drag floating layouts.

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
