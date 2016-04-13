#!/usr/bin/kano-splash /usr/share/make-snake/media/splash.png /bin/sh
# snake-launch-overworld.sh
#
# Copyright (C) 2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPLv2
#
# This is the game launcher script used by kano-overworld

rxvt -title 'Make Snake' -e make-snake &
pid=$!

sleep 1
wmctrl -r "Make Snake" -b toggle,maximized_vert,maximized_horz

wait $pid
