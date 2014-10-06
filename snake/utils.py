#!/usr/bin/env python

# utils.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
#

import os

from kano_world.share import upload_share
from kano.network import is_internet
from kano_world.functions import login_using_token
from kano_profile.badges import increment_app_state_variable_with_dialog
from kano.utils import run_cmd
from theme import update_theme_list, DEFAULT_THEMES, app_dir


def print_themes(show_default=True, terminate=True):
    # List of default themes
    default_themes = "{{3Default themes}}: "
    for l in DEFAULT_THEMES:
        default_themes += '{{2' + l + "}} | "
    default_themes = default_themes[:-2]
    # List of custom themes
    custom_themes = "{{3Custom themes}}: "
    theme_list = update_theme_list()
    for l in theme_list:
        # Remove .xml extension
        l = os.path.splitext(l)[0]
        custom_themes += '{{2' + l + "}} | "
    custom_themes = custom_themes[:-2]
    # Print info
    default_themes, _, _ = run_cmd('colour_echo "%s"' % default_themes)
    custom_themes, _, _ = run_cmd('colour_echo "%s"' % custom_themes)
    # Print default themes
    print "\n"
    if show_default:
        print "    " + default_themes.strip('\n')
    # Print custom themes
    print "    " + custom_themes.strip('\n') + '\n'
    if terminate:
        exit(2)


def check_valid_theme(theme):
    if theme in DEFAULT_THEMES:
        return
    theme_list = update_theme_list()
    if not theme.endswith('.xml'):
        theme += '.xml'
    if theme not in theme_list:
        coloured_error, _, _ = run_cmd('colour_echo "{{8 x }} {{7 error: }}"')
        print "\n    " + coloured_error.strip('\n') + \
              'Theme %s not found (names are case sensitive)\n' % theme
        exit(2)


def share_theme():
    # Check for internet
    if not is_internet():
        coloured_error, _, _ = run_cmd('colour_echo "{{8 x }} {{7 error: }}"')
        print "\n    " + coloured_error.strip('\n') + 'You need internet connection'
        exit(2)
    # Check for login
    success, _ = login_using_token()
    if not success:
        coloured_error, _, _ = run_cmd('colour_echo "{{8 x }} {{7 error: }}"')
        print "\n    " + coloured_error.strip('\n') + 'You need to login to Kano World'
        exit(2)
    # Print themes
    print_themes(False, False)
    # Select theme dialogue
    message = "    1) Select a theme: "
    theme = raw_input(message)
    theme += '.xml'
    # Check theme exists
    check_valid_theme(theme)
    # Select title
    message = "    2) Write a title: "
    title = raw_input(message)
    if not title:
        title = 'My snake'
    # Select description
    message = "    3) Write a description: "
    description = raw_input(message)
    # Create json
    create_share_json(theme, title, description)
    # Share
    filepath = os.path.join(app_dir, theme)
    success, msg = upload_share(filepath, title, 'make-snake')
    if not success:
        coloured_error, _, _ = run_cmd('colour_echo "{{8 x }} {{7 error: }}"')
        print "\n    " + coloured_error.strip('\n') + 'Sharing of %s failed. %s\n' % (theme, msg)
        exit(2)
    message, _, _ = run_cmd('colour_echo "{{4 + }} {{3 You have shared your theme successfully }}"')
    print "\n    " + message.strip('\n')
    increment_app_state_variable_with_dialog('make-snake', 'shared', 1)
    exit(2)


def reset_game():
    # We use 10 as reset level, so the user does not lose badges and level
    os.system("kano-profile-cli save_app_state_variable make-snake level 10")
    exit(0)


def create_share_json(filename, title, description):
    import json

    # Remove .xml extension
    filename = os.path.splitext(filename)[0]
    # Data
    metadata = {'title': title, 'description': description}
    data = json.dumps(metadata)
    # Create file
    filepath = os.path.join(app_dir, filename + '.json')
    with open(filepath, 'w+') as f:
        f.write(data)
