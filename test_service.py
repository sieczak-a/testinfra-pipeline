import testinfra

def test_sshd_service(host):
    ssh = host.service("sshd")
    assert ssh.is_running
    assert ssh.is_enabled


def test_docker_service(host):
    docker = host.service('docker')
    assert docker.is_running
    assert docker.is_enabled
