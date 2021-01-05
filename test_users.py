import testinfra
def test_docker_group(host):
    assert host.group("docker").exists


def test_nickfury(host):
    nickfury = host.user('vagrant')
    assert nickfury.exists

    nickfury_gids = host.user('vagrant').gids
    docker_gid = host.group("docker").gid
    assert docker_gid in nickfury_gids
