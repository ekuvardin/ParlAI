#!/usr/bin/env python3

# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
# Download and build the data if it does not exist.

import parlai.core.build_data as build_data
import os


def build(opt):
    dpath = os.path.join(opt['datapath'], 'WoZ')
    version = 'None'

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        fnames = ['woz_test_en.json', 'woz_train_en.json', 'woz_validate_en.json']
        for fname in fnames:
            url = 'https://github.com/nmrksic/' \
                  'neural-belief-tracker/raw/master/data/woz/'
            + fname
        build_data.download(url, dpath, fname)

    # Mark the data as built.
    build_data.mark_done(dpath, version_string=version)
