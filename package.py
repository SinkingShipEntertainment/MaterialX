name = "materialx"

authors = [
    "Lucasfilm"
]

version = "1.38.0"

description = \
    """
    MaterialX is an open standard for transfer of rich material and look-development
    content between applications and renderers.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

# Modify the CMakeLists to reflect python versions being used here
variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7"],
]

# NOTE: Remember to run: git submodule update --init --recursive

# Pass cmake arguments to the REZ build system:
# rez-build -i -- -DMATERIALX_PYTHON_EXECUTABLE:FILEPATH=${REZ_PYTHON_ROOT}/bin/python
# rez-release -- -DMATERIALX_PYTHON_EXECUTABLE:FILEPATH=${REZ_PYTHON_ROOT}/bin/python

uuid = "repository.MaterialX"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.MATERIALX_ROOT = "{root}"
    env.MATERIALX_LOCATION = "{root}"

    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
