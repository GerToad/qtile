from libqtile import layout
from libqtile.config import Match

layout_theme = {"border_width": 1,
                "margin": 4,
                "border_focus": '#81a1c1',
                "border_normal": "#4c566a"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
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

floating_layout = layout.Floating(
    float_rules=[
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
        Match(wm_class='gnome-calculator'), #Calculator
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],border_focus = '#81a1c1'
)
