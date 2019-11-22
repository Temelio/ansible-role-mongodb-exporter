"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mongodb_exporter_service(host):
    """
    Check if mongodb_exporter service is started and enabled
    """

    services = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        services = ['mongodb-exporter']

    for service in services:
        assert host.service(service).is_enabled

        assert host.service(service).is_running


def test_system_user(host):
    """
    Check if system user exists
    """
    if host.system_info.codename == 'bionic':
        assert host.user('mongodb-exporter').exists
        assert host.user('mongodb-exporter').group == 'mongodb-exporter'
        assert host.user('mongodb-exporter').shell == '/sbin/nologin'


def test_config_files(host):
    """
    Check if configuration files exists
    """

    config_files = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        config_files = [
            '/etc/mongodb-exporter/mongodb-exporter.config',
        ]

    for config_file in config_files:
        assert host.file(config_file).exists
        assert host.file(config_file).user == 'mongodb-exporter'
        assert host.file(config_file).group == 'mongodb-exporter'
        assert host.file(config_file).mode == 0o600


def test_mongodb_exporter_sockets(host):
    """
    Check if mongodb-exporter is listening
    """

    # mongodb-exporter
    assert host.socket('tcp://127.0.0.1:9001').is_listening
