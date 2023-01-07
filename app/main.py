import os
import shutil
import subprocess
import sys

tmp_dir = "/home/tmp"
executable_file = "/usr/local/bin/docker-explorer"


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    # create tmp dir & copy executable into tmp dir
    os.makedirs(f"{tmp_dir}{os.path.dirname(executable_file)}", exist_ok=True)
    shutil.copy(executable_file, f"{tmp_dir}{executable_file}")

    # change root dir
    os.chroot(tmp_dir)

    completed_process = subprocess.run([command, *args], capture_output=True)
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    if completed_process.returncode != 0:
        sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
