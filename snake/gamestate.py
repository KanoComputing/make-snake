#!/usr/bin/env python

# gamestate.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

import kano.profile as kp

app_name = 'make-snake'
state = dict()


def load_state():
    global state

    try:
        state = kp.load_app_state(app_name)
        init_states = kp.get_gamestate_variables(app_name)

        # loop through all states and initialise them with zero
        for s in init_states:
            if s not in state:
                state[s] = 0
    except Exception:
        pass


def save_state():
    global state

    try:
        kp.save_app_state(app_name, state)
    except Exception:
        pass
