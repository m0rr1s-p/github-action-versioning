from semver.version import Version
import os

def set_github_action_output(name, value):
    with open(os.path.abspath(os.environ['GITHUB_OUTPUT']), 'a') as f:
        f.write(f'{name}={value}\n')

def  increment_version(version, increment_type, max_increment):
    try:
        ver = Version.parse(version)
    except ValueError:
        print(f"::warning title=invalid version::{version} is not valid semver")
        return version
    match increment_type:
        case "patch":
            if ver.patch < max_increment:
                return ver.bump_patch()
            elif ver.patch >= max_increment > ver.minor:
                return ver.bump_minor()
            else:
                return ver.bump_major()
        case "minor":
            if ver.minor < max_increment:
                return ver.bump_minor()
            else:
                return ver.bump_major()
        case "major":
            return ver.bump_major()
        case _:
            print(f"::warning title=invalid increment type::{increment_type} is not valid")
            return version


def main():
    input_version = os.environ.get("INPUT_VERSION")
    input_max_increment = int(os.environ.get("INPUT_MAX_INCREMENT"))
    input_increment_type = os.environ.get("INPUT_INCREMENT_TYPE")

    set_github_action_output('version', increment_version(input_version, input_increment_type, input_max_increment))

if __name__ == "__main__":
    main()
