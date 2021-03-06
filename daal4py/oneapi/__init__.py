#!/usr/bin/env python
#===============================================================================
# Copyright 2020-2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import platform
if "Windows" in platform.system():
    import os
    import sys
    import site
    path_to_env = site.getsitepackages()[0]
    path_to_libs = os.path.join(path_to_env, "Lib", "site-packages", "daal4py", "oneapi")
    print('libs:', path_to_libs)
    if sys.version_info.minor >= 8:
        os.add_dll_directory(path_to_libs)
    os.environ['PATH'] += os.pathsep + path_to_libs

from _oneapi import sycl_context, sycl_buffer, is_in_sycl_ctxt
