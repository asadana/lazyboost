#  LazyBoost
#  Copyright (C) 2021  Ankit Sadana
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pyperclip

from lazyboost import log

_cli_logger = log.console_logger()


def update_clipboard_tags():
    current_clipboard = pyperclip.paste()
    current_clipboard = current_clipboard.splitlines()
    current_clipboard = [i for i in current_clipboard if i]
    current_clipboard.sort()

    _cli_logger.info(f"Cleaned up Etsy tags: {_etsy_description_tags(current_clipboard)}")
    _cli_logger.info(f"Cleaned up Facebook tags: {_facebook_post_description_tags(current_clipboard)}")
    pyperclip.copy(_etsy_description_tags(current_clipboard))
    pyperclip.copy(_facebook_post_description_tags(current_clipboard))


def _etsy_description_tags(tag_list: list) -> str:
    return ", ".join(tag_list)


def _facebook_post_description_tags(tag_list: list) -> str:
    fb_tag_list = []
    for i in tag_list:
        fb_tag_list.append("#" + i.replace(" ", "").replace("'", ""))

    return " ".join(fb_tag_list)

