#!/usr/bin/python
"""
Ansible module for sasl_password management.
"""
import os
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: sasl_password 
short_description: Manage your sasl_password map.
'''

EXAMPLES = '''
- name: Update sasl_password
  sasl_password:
    name: "/etc/sasl_password"
    host: "mailgrid.org"
    user: "postmaster"
    password: "..."
'''

RETURNS = '''
'''

def main():
    """
    Implement postmap for Ansible.
    """
    args = {
        'name': {'required': True, 'type': 'str'},
        'host': {'required': True, 'type': 'str'},
        'port': {'type': 'int', 'default': 25},
        'user': {'required': True, 'type': 'str'},
        'password': {'required': True, 'type': 'str', 'no_log': True}
    }
    module = AnsibleModule(argument_spec=args, supports_check_mode=True)
    changed = False
    old_msg = ""
    vals = {}
    for key in args:
        vals[key] = module.params[key]

    msg = "[%s]:%s\t%s:%s" % (vals['host'], vals['port'], vals['user'], vals['password'])
    with os.popen('postmap -s ' + vals['name'], 'r') as old_file:
        old_msg = old_file.read().strip()
    changed = (msg != old_msg)

    if changed and not module.check_mode:
        os.unlink(vals['name'] + '.db')
        with os.popen('postmap -i ' + vals['name'], 'w') as new_file:
            new_file.write(msg + '\n')
    module.exit_json(changed=changed, new_value=msg, old_value=old_msg)


if __name__ == '__main__':
    main()
