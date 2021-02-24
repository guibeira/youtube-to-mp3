import asyncio
import functools
import itertools
import time

DONWLOAD_COMMAND = "youtube-dl  -x -i -q --audio-format mp3 --audio-quality 0 --embed-thumbnail --no-playlist --no-warnings {}"


async def spin(msg):
    for char in itertools.cycle("⠇⠋⠙⠸⠴⠦"):
        status = msg + " " + char
        print(status, flush=True, end="\r")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    print(" " * len(status), end="\r")


def spinner_msg(msg):
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
            spinner = asyncio.create_task(spin(msg))
            return await func(*args)
            spinner.cancel()

        return wrapped

    return wrapper


async def runner(cmd, show_output=False):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()

    if not show_output:
        return

    print(f"[{cmd!r} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


async def dowload_music(url_music):
    cmd = DONWLOAD_COMMAND.format(url_music)
    await runner(cmd)


@spinner_msg("Installing dependencies!")
async def install_dependencies():
    await runner("pip install --upgrade youtube-dl")


@spinner_msg("Downloading musics!")
async def donwload_musics(musics):
    tasks = [dowload_music(music) for music in musics]
    await asyncio.gather(*tasks)


def main():
    t0 = time.perf_counter()
    asyncio.run(install_dependencies())
    musics = open("musics.txt")
    asyncio.run(donwload_musics(set(musics.readlines())))
    dt = time.perf_counter() - t0
    print(f"Finished in : {dt:0.3}s")


if __name__ == "__main__":
    main()
