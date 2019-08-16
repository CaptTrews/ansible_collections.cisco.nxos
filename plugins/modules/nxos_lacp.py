#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for nxos_lacp
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: nxos_lacp
version_added: 2.9
short_description: Manage Global Link Aggregation Control Protocol (LACP) on Cisco NX-OS devices.
description: This module manages Global Link Aggregation Control Protocol (LACP) on NX-OS devices.
author: Trishna Guha (@trishnaguha)
notes:
  - Tested against NXOS 7.3.(0)D1(1) on VIRL.
  - Feature lacp should be enabled for this module.
options:
  config:
    description: LACP global options.
    type: dict
    suboptions:
      system:
        description:
          - LACP system options
        type: dict
        suboptions:
          priority:
            description:
              - The system priority to use in LACP negotiations.
            type: int
          mac:
            description:
              - MAC address to be used for the LACP Protocol exchanges
            type: dict
            suboptions:
              address:
                description:
                  - MAC-address (FORMAT :xxxx.xxxx.xxxx).
                type: str
              role:
                description:
                  - The role for the Switch.
                type: str
                choices: ['primary', 'secondary']
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
      - merged
      - replaced
      - deleted
    default: merged
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#

- name: Merge provided configuration with device configuration.
  nxos_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
    state: merged

# After state:
# ------------
#
# lacp system-priority 10
# lacp system-mac 00c1.4c00.bd15


# Using replaced

# Before state:
# -------------
#
# lacp system-priority 10

- name: Replace device global lacp configuration with the given configuration.
  nxos_lacp:
    config:
      system:
        mac:
          address: 00c1.4c00.bd15
    state: replaced

# After state:
# ------------
#
# lacp system-mac 00c1.4c00.bd15


# Using deleted

# Before state:
# -------------
#
# lacp system-priority 10

- name: Delete global LACP configurations.
  nxos_lacp:
    state: deleted

# After state:
# ------------
#


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lacp system-priority 15', 'lacp system-mac 00c1.4c00.bd15 role primary']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.lacp.lacp import (
    LacpArgs,
)

from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.lacp.lacp import (
    Lacp,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=LacpArgs.argument_spec, supports_check_mode=True
    )

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
