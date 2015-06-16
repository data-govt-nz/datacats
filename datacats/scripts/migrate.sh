#!/bin/bash

# Copyright 2014-2015 Boxkite Inc.

# This file is part of the DataCats package and is released under
# the terms of the GNU Affero General Public License version 3.0.
# See LICENSE.txt or http://www.fsf.org/licensing/licenses/agpl-3.0.html

set -e

echo "${@:3}"

for f in "${@:3}"; do
    [ -e "$1/$f" ] && mv "$1/$f" "$2/$f"
done
