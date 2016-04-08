#!/usr/bin/kano-splash /usr/share/make-snake/media/splash.png /bin/sh
rxvt -title 'Make Snake' -e make-snake &
pid=$!

sleep 1
wmctrl -r "Make Snake" -b toggle,maximized_vert,maximized_horz

while kill -0 $pid 2> /dev/null; do
    sleep 1
done
