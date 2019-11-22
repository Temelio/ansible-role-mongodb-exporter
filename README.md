# mongodb-exporter

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/temelio/mongodb-exporter.svg?branch=master)](https://travis-ci.org/temelio/mongodb-exporter)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-mongodb-exporter/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-mongodb-exporter/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-mongodb-exporter/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-mongodb-exporter/)
[![Ansible Role](https://img.shields.io/ansible/role/.svg)](https://galaxy.ansible.com/Temelio/mongodb-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/Temelio/ansible-role-mongodb-exporter.svg)](https://github.com/Temelio/ansible-role-mongodb-exporter/tags)

Install mongodb-exporter package.

## Requirements

This role requires Ansible 2.7 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for mongodb-exporter role

is_initd_managed_system: "{{ _is_initd_managed_system | default(False) }}"
is_systemd_managed_system: "{{ _is_systemd_managed_system | default(False) }}"

mongodb_exporter_service_systemd:
  - src: "{{ role_path }}/templates/services/systemd.service.j2"
    dest: "{{ mongodb_exporter_folders_paths.systemd }}/{{ mongodb_exporter_service_name }}.service"

mongodb_exporter_service_initd:
  - src: "{{ role_path }}/templates/services/init.d.j2"
    dest: "{{ mongodb_exporter_folders_paths.initd }}/{{ mongodb_exporter_service_name }}"

# General
mongodb_exporter_system_user: 'mongodb-exporter'
mongodb_exporter_system_group: 'mongodb-exporter'

# Packages
# Additional packages to setup as role/exporter dependencies
mongodb_exporter_system_packages:
  - name: 'ca-certificates'
    state: 'present'
  - name: 'tar'
    state: 'present'
mongodb_exporter_install_package: True
mongodb_exporter_get_package_from_url: True
mongodb_exporter_manager_url: "{{ _mongodb_exporter_manager_url | default('') }}"
mongodb_exporter_package_name: "{{ _mongodb_exporter_package_name }}"
mongodb_exporter_package_path: "{{ mongodb_exporter_folders_paths.tmp }}/{{ mongodb_exporter_service_name }}"
# mongodb_exporter_package_url: "{{ mongodb_exporter_manager_url }}/download/agent/automation/{{ mongodb_exporter_package_name }}"
mongodb_exporter_package_state: 'present'

# Paths
mongodb_exporter_folders_paths:
  config: "{{ _mongodb_exporter_os_base_etc_path }}/{{ mongodb_exporter_service_name }}"
  initd: "{{ _mongodb_exporter_os_base_initd_path }}"
  systemd: "{{ _mongodb_exporter_os_base_systemd_path }}"
  tmp: "{{ _mongodb_exporter_os_base_tmp_path }}"
  log: "/var/log/{{ mongodb_exporter_service_name }}"
  bin: '/usr/local/bin'
  pid: '/var/run'

# Configuration
mongodb_exporter_version: '0.10.0'
mongodb_exporter_github_account: 'percona'
mongodb_exporter_base_url: "https://github.com/{{ mongodb_exporter_github_account }}/mongodb_exporter"
# Exporter download URL
mongodb_exporter_release_url: "{{ mongodb_exporter_base_url }}/releases/download/v{{ mongodb_exporter_version }}/mongodb_exporter-{{ mongodb_exporter_version }}.{{ ansible_system |lower }}-amd64.tar.gz"
mongodb_exporter_mongo_username: 'mongodbexporter'
mongodb_exporter_mongo_pwd: 'changeme'
mongodb_exporter_mongo_address: '127.0.0.1'
mongodb_exporter_mongo_port: '27017'
mongodb_exporter_mongo_auth_database: 'admin'
# MongoDB URI in format [mongodb://][user:pass@]host1[:port1][,host2[:port2],...][/database][?options]
# set this variable for init.d system
mongodb_exporter_mongodb_uri: 'mongodb://127.0.0.1:27017'
# Max number of pooled connections to the database
mongodb_exporter_mongodb_max_connections: 1
# Amount of time to wait for a non-responding socket to the database before it is forcefully closed
mongodb_exporter_mongodb_socket_timeout: 3s
# Amount of time an operation with this session will wait before returning an error in case a connection to a usable server can't be established
mongodb_exporter_mongodb_sync_timeout: 1m
# Specifies the database in which the user is created
mongodb_exporter_authentification_database: 'admin'

# List of environment variables to set before starting exporter
mongodb_exporter_env_vars:
  - name: 'MONGODB_URI'
    value: "mongodb://{{ mongodb_exporter_mongo_username }}:{{ mongodb_exporter_mongo_pwd }}@{{ mongodb_exporter_mongo_address }}/{{ mongodb_exporter_mongo_port }}/{{ mongodb_exporter_mongo_auth_database }}"
#  - { name: HTTP_AUTH,   value: "{{ mongodb_exporter_mongo_username }}:{{ mongodb_exporter_mongo_pwd }}" }             # used to enable HTTP basic authentication

# Address to listen on for web interface and telemetry
mongodb_exporter_web_listen_address: ':9001'
# Path under which to expose metrics
mongodb_exporter_web_telemetry_path: '/metrics'

# Enable collection of database metrics
mongodb_exporter_collect_database: false
# Enable collection of collection metrics
mongodb_exporter_collect_collection: false
# Enable collection of table top metrics
mongodb_exporter_collect_topmetrics: false
# Enable collection of per index usage stats
mongodb_exporter_collect_indexusage: false
# Enable tls connection with mongo server
mongodb_exporter_mongodb_tls: false

# Services management
mongodb_exporter_service_name: "{{ _mongodb_exporter_service_name }}"
mongodb_exporter_service_state: 'started'
mongodb_exporter_service_enabled: True
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: temelio.mongodb-exporter }
```

## License

MIT

## Author Information

Lise Machetel (for Temelio company)
- https://temelio.com
- admin [at] temelio.com
