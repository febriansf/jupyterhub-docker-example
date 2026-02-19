import os

c = get_config()

c.JupyterHub.bind_url = "http://0.0.0.0:8000"

from nativeauthenticator import NativeAuthenticator

c.JupyterHub.authenticator_class = NativeAuthenticator

c.NativeAuthenticator.enable_signup = True

c.NativeAuthenticator.open_signup = False

c.Authenticator.admin_users = {"admin"}

c.Authenticator.allow_all = True

c.Authenticator.allow_existing_users = True

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Enable suport for CUDA
c.DockerSpawner.image = os.environ.get("DOCKER_JUPYTER_IMAGE", "nvidia/cuda:12.9.1-cudnn-runtime-ubuntu24.04")

c.DockerSpawner.notebook_dir = "/home/jovyan"
c.DockerSpawner.volumes = {
    "jupyterhub-user-{username}": "/home/jovyan"
}

c.DockerSpawner.network_name = "jupyter_default"
c.DockerSpawner.use_internal_ip = True

# GPU config
c.DockerSpawner.extra_host_config = {
    "device_requests": [
        {
            "Driver": "nvidia",
            "Count": 1,
            "Capabilities": [["gpu"]]
        }
    ]
}

c.DockerSpawner.environment = {
    "NVIDIA_VISIBLE_DEVICES": "all",
    "NVIDIA_DRIVER_CAPABILITIES": "compute,utility"
}

c.JupyterHub.hub_ip = os.environ.get("HUB_IP", "jupyterhub")

c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"
