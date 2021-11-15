from omnitools import blake2bd
import userscloud
import time
import re


done = 0
prev_fp = None


def progress(fp, size, x):
    global done
    global prev_fp
    global start
    if not prev_fp:
        prev_fp = fp
    elif prev_fp != fp:
        done = 0
        prev_fp = fp
        start = time.time()
        print()
    done += len(x)
    print("\r", fp, time.time()-start, done/((time.time()-start) or 1)/1024/1024, done/size*100, end="")


key = "my secret 1"
iv = blake2bd("my secret 2", digest_size=8)
c = userscloud.UC_FTP(
    timeout=10,
    unwrap_sslsocket_after_completed_transfer=False,
    debug=True,
)
c.login()
print(c.list_dir("/04"))
fn = "zip.zip"
buffer = 8*1024*10
start = time.time()
# c.raw_upload("/src/{}".format(fn), "/04", buffer, progress)
# c.raw_upload("/src/{}".format(fn), "/04", buffer, progress, key=key, iv=iv)
print(time.time()-start)
start = time.time()
# c.raw_download("/tmp", "/04/{}".format(fn), buffer, progress)
# c.raw_download("/tmp", "/04/{}".format(fn), buffer, progress, key=key, iv=iv)
print(time.time()-start)
# c.queue_upload(r"/phone", re.compile("^Screenshots.*?2015-11-23"), buffer, progress, key=key, iv=iv)
# input()
# c.download("/tmp", "/Screenshots", buffer, progress, key=key, iv=iv)
# c.upload("/src", re.compile(r".*\.txt$"), buffer, progress, dry_run=True, key=key, iv=iv)
