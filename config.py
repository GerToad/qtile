# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy


mod = "mod4"
myTerm = 'alacritty'

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

##############################################
################ SETTINGS ####################
##############################################

    KeyChord([mod], "q", [
        Key([], "s", lazy.spawn(myTerm + " -e systemctl suspend")),
        Key([], "o", lazy.spawn(myTerm + " -e systemctl poweroff")),
        Key([], "b", lazy.spawn(myTerm + " -e sudo chmod 666 /sys/class/backlight/intel_backlight/brightness")),
    ]),

    # ------------ qtile ---------------

    # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
    # lazy.spawn("emacsclient -c -a 'emacs'"),
    # lazy.spawn("./dmscripts/dm-confedit"),
    KeyChord([mod],"c", [
        Key([], "c",
            lazy.spawn(myTerm + ' -e tty-clock'),
            desc='Launch qtile config'
        ),
    ]),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    KeyChord([mod], "a", [
        Key([], "i", lazy.spawn("nautilus"), desc="Launch file manager"),
        Key([], "y", lazy.spawn("spotify"), desc="Launch spotify"),
        Key([], "f", lazy.spawn("firefox"), desc="Launch firefox"),
        Key([], "s", lazy.spawn("steam"), desc="Launch steam"),
        Key([], "b", lazy.spawn("brave-browser"), desc="Launch brave"),
        Key([], "d", lazy.spawn("gnome-todo"), desc="Launch To Do"),
        Key([], "t", lazy.spawn("TelegramDesktop"), desc="Launch Telegram"),
    ]),

    Key([mod], "o",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "p",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),

    # Key([mod, 'control'], 'a', lazy.spawn('gnome-screensaver-command -l')),
    # Key([mod, 'control'], 'z', lazy.spawn('gnome-session-quit --logout --no-prompt')),
    # Key([mod, 'shift', 'control'], 'z', lazy.spawn('gnome-session-quit --power-off')),

# ------------ Hardware Configs ------------
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([mod], "F3", lazy.spawn("brightnessctl set +5%")),
    Key([mod], "F2", lazy.spawn("brightnessctl set 5%-")),
##############################################
############## SCREENSHOTS ###################
##############################################

    Key([mod], "Print", lazy.spawn("xfce4-screenshooter")),
    Key([], "Print", lazy.spawn("gnome-screenshot")),
]

###Groups###
groups = [Group(i) for i in [
    " 爵 ", "  ", "  ", "  ", "  ", "  ", " ", "  ", "  ",
]]
#漣爵

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


layout_theme = {"border_width": 1,
                "margin": 4,
                "border_focus": '#81a1c1',
                "border_normal": "4c566a"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(
        # font = "Ubuntu",
        # fontsize = 10,
        # sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
        # section_fontsize = 10,
        # border_width = 2,
        # bg_color = "1c1f24",
        # active_bg = "c678dd",
        # active_fg = "000000",
        # inactive_bg = "a9a1e1",
        # inactive_fg = "1c1f24",
        # padding_left = 0,
        # padding_x = 0,
        # padding_y = 5,
        # section_top = 10,
        # section_bottom = 20,
        # level_shift = 8,
        # vspace = 3,
        # panel_width = 200
    # ),
    layout.Floating(**layout_theme)
]

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
#""

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
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e apt list --upgradable')},
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
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='org.gnome.Nautilus'), #Nautilus
    Match(wm_class='Telegram'), #Telegram
    Match(wm_class='spotify'), #Spotify
    Match(wm_class='standard notes'), #Notes
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
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
