import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    "string, status", [
        ("APT::Periodic::Update-Package-Lists", True),
        ("APT::Periodic::Download-Upgradeable-Packages", True),
        ("APT::Periodic::AutocleanInterval", True),
        ("APT::Periodic::Unattended-Upgrade", True),
    ]
)
def test_configuration(host, string, status):
    config = host.file('/etc/apt/apt.conf.d/10periodic')

    assert config.exists
    assert config.contains(string) is status


def test_configuration_upgrade(host):
    config = host.file('/etc/apt/apt.conf.d/50unattended-upgrades')

    assert config.exists
    assert config.contains(
        """Unattended-Upgrade::Mail "noop@tangrama.com.br";"""
    )
