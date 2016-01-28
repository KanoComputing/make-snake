# gamestate.py
#
# Copyright (C) 2013-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
from kano_profile.badges import update_upwards_with_dialog, \
    increment_app_state_variable_with_dialog

STATUS = {
    'longest_snake': 0,
    'total_length': 0,
    'total_number_of_apples': 0,
    'total_score': 0,
    'highest_score': 0
}


def update_profile_stats():
    update_upwards_with_dialog(
        'make-snake', 'longest_snake', STATUS['longest_snake']
    )
    update_upwards_with_dialog(
        'make-snake', 'highest_score', STATUS['highest_score']
    )
    increment_app_state_variable_with_dialog(
        'make-snake', 'total_length', STATUS['total_length']
    )
    increment_app_state_variable_with_dialog(
        'make-snake', 'total_number_of_apples', STATUS['total_number_of_apples']
    )
    increment_app_state_variable_with_dialog(
        'make-snake', 'total_score', STATUS['total_score']
    )
