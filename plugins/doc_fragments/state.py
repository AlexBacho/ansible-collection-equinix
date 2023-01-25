# Copyright: (c) 2021, Equinix Metal
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    # Standard documentation
    DOCUMENTATION = '''
    options:
        state:
            description:
                - The state of the resource.
            type: str
            default: present
            choices:
                - present
                - absent
    '''
