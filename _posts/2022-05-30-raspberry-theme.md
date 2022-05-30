---
title: Raspberry Pi OS Customization
date: 2022-05-30 19:00
categories: [Linux, Raspberry Pi OS]
tags: [linux, raspberry, raspbian, customization]
---

# Install icon theme and theme manager
```bash
sudo apt install arc-theme papirius-icon-theme
lxappearance
```
This will install a dark theme and a pleasant icon theme, then you can change the general OS appearance in `lxappearance`.
Here is my `~/.config/lxterminal/lxterminal.conf`:
```bash
[general]
fontname=Fira Code Light 14
selchars=-A-Za-z0-9,./?%&#:_
scrollback=1000
bgcolor=rgb(35,35,47)
fgcolor=rgb(189,195,199)
palette_color_0=rgb(80,80,95)
palette_color_1=rgb(255,86,142)
palette_color_2=rgb(100,222,131)
palette_color_3=rgb(239,255,115)
palette_color_4=rgb(115,169,255)
palette_color_5=rgb(148,111,247)
palette_color_6=rgb(98,198,218)
palette_color_7=rgb(238,232,213)
palette_color_8=rgb(80,80,95)
palette_color_9=rgb(255,86,142)
palette_color_10=rgb(100,222,131)
palette_color_11=rgb(239,255,115)
palette_color_12=rgb(115,169,255)
palette_color_13=rgb(148,111,247)
palette_color_14=rgb(98,198,218)
palette_color_15=rgb(253,246,227)
color_preset=Custom
disallowbold=false
cursorblinks=true
cursorunderline=true
audiblebell=false
tabpos=top
geometry_columns=80
geometry_rows=24
hidescrollbar=false
hidemenubar=false
hideclosebutton=false
hidepointer=false
disablef10=false
disablealt=false
disableconfirm=false

[shortcut]
new_window_accel=<Primary><Shift>n
new_tab_accel=<Primary><Shift>t
close_tab_accel=<Primary><Shift>w
close_window_accel=<Primary><Shift>q
copy_accel=<Primary><Shift>c
paste_accel=<Primary><Shift>v
name_tab_accel=<Primary><Shift>i
previous_tab_accel=<Primary>Page_Up
next_tab_accel=<Primary>Page_Down
move_tab_left_accel=<Primary><Shift>Page_Up
move_tab_right_accel=<Primary><Shift>Page_Down
zoom_in_accel=<Primary><Shift>plus
zoom_out_accel=<Primary><Shift>underscore
zoom_reset_accel=<Primary><Shift>parenright
```