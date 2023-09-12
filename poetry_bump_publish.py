import subprocess


if __name__ == "__main__":

    result = subprocess.run(["poetry", "version"], stdout=subprocess.PIPE)
    module, version = result.stdout.decode('utf-8').split()
    major, minor, patch = version.split(".")

    new_patch = int(patch) + 1
    new_version = ".".join([major, minor, str(new_patch)])

    print(f"Bumping up patch from {module}...")
    print(f"From version ({version}) to ({new_version})")

    subprocess.run(["poetry", "version", new_version])
    subprocess.run(["poetry", "build"]) 
    subprocess.run(["poetry", "publish", "-r", "test-pypi"])
