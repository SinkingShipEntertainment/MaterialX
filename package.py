name = "materialx"

authors = [
    "Lucasfilm"
]

version = "1.38.9"

description = \
    """
    MaterialX is an open standard for transfer of rich material and look-development
    content between applications and renderers.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

# Modify the CMakeLists to reflect python versions being used here
variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
]

# NOTE: Remember to run (after first time cloning): git submodule update --init --recursive

uuid = "repository.MaterialX"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.MATERIALX_ROOT = "{root}"
    env.MATERIALX_LOCATION = "{root}"

    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
