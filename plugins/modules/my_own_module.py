#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: Creates a text file on the remote host

version_added: "1.0.0"

description: This module creates a text file on the remote host with the specified content.

options:
    path:
        description: The path where the file should be created on the remote host.
        required: true
        type: str
    content:
        description: The content to write to the file.
        required: true
        type: str

author:
    - @ufilin
'''

EXAMPLES = r'''
- name: Create a text file
  my_namespace.my_collection.my_test:
    path: /tmp/example.txt
    content: "Hello, world!"

- name: Create a file with multiple lines
  my_namespace.my_collection.my_test:
    path: /opt/config/app.conf
    content: |
      server=localhost
      port=8080
      debug=true
'''

RETURN = r'''
path:
    description: The path to the file that was created or modified.
    type: str
    returned: always
    sample: '/tmp/example.txt'
content:
    description: The content that was written to the file.
    type: str
    returned: always
    sample: 'Hello, world!'
changed:
    description: Whether the file was created or changed.
    type: bool
    returned: always
    sample: true
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    
    result['path'] = path
    result['content'] = content

    file_exists = os.path.exists(path)
    current_content = None
    
    if file_exists:
        try:
            with open(path, 'r') as f:
                current_content = f.read()
        except (IOError, OSError) as e:
            module.fail_json(msg="Failed to read existing file: %s" % str(e), **result)
    
    if not file_exists or current_content != content:
        if module.check_mode:
            result['changed'] = True
            module.exit_json(**result)
        
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except (IOError, OSError) as e:
                module.fail_json(msg="Failed to create directory %s: %s" % (directory, str(e)), **result)
        
        try:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except (IOError, OSError) as e:
            module.fail_json(msg="Failed to write to file %s: %s" % (path, str(e)), **result)
    else:
        result['changed'] = False

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
