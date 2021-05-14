# Tangrama: Common setup

Role to install base packages and proceed with a common setup for Ubuntu servers.

## Packages

This role install the following packages:

* aptitude
* curl
* iproute2
* needrestart
* openssh-server
* python3-apt
* python3-minimal
* rsync

It is important to mention *openssh-server* should always be available in remote servers, but we force its installation here to make sure tests with *molecule* to be successful.

## Role Variables

### fqdn

FQDN for the host

```yaml
    fqdn: plone.tangrama.com.br
```

### ssh_port

Port number to be used by *sshd* process.

```yaml
    ssh_port: 9923
```

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - { role: tangrama.common }
      vars:
        ssh_port: 9923
```

## Testing

This role uses [molecule](https://molecule.readthedocs.io/) for linting and testing.

```shell
    molecule test
```

## License

GPLv2

## Author Information

* Tangrama (tangrama at simplesconsultoria dot com dot br)
