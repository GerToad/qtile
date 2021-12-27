##############################################
################## KEYS ######################
##############################################

from libqtile.config import Key, KeyChord
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
        Key([], "r", lazy.spawn(myTerm + " -e reboot")),
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

