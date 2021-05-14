import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_enabled(host):
    service = host.service('ssh')

    assert service.is_enabled


def test_service_ports(host):
    assert not host.socket("tcp://0.0.0.0:22").is_listening
    assert host.socket("tcp://0.0.0.0:9923").is_listening


@pytest.mark.parametrize(
    "string, status", [
        ("Port 9923", True),
        ("PasswordAuthentication no", True),
        ("X11Forwarding no", True),
        ("ClientAliveCountMax 0", True),
        ("ClientAliveCountMax 0", True),
        ("ClientAliveInterval 300", True),
    ]
)
def test_configuration(host, string, status):
    config = host.file('/etc/ssh/sshd_config')

    assert config.exists
    assert config.contains(string) is status
