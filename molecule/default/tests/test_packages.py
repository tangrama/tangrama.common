import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    "package_name", [
        "acl",
        "aptitude",
        "curl",
        "docker.io",
        "iproute2",
        "needrestart",
        "openssh-server",
        "python3-apt",
        "python3-minimal",
        "rsync",
        "unattended-upgrades",
    ]
)
def test_package_installed(host, package_name):
    pkg = host.package(package_name)

    assert pkg.is_installed
