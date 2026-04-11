import docker

client = docker.DockerClient(base_url='npipe:////./pipe/docker_engine')
output = client.containers.run("alpine", ["echo", "hello", "world"])
print(output.decode())