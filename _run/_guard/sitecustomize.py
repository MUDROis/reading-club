
import os, shutil, pathlib
_ALLOW = [os.path.realpath(p) for p in os.environ.get("DEWIAR_ALLOW_DEL", "").split(os.pathsep) if p]
def _ok(p):
    try:
        r = os.path.realpath(os.fspath(p))
    except Exception:
        return False
    return any(r == a or r.startswith(a.rstrip(os.sep) + os.sep) for a in _ALLOW)
def _wrap(f, name):
    def g(p, *a, **k):
        if k.get("dir_fd") is None and not _ok(p):     # dir_fd — изнутри rmtree, корень уже проверен
            raise PermissionError(f"Dewiar: удалять можно только в папке задачи и во временной папке, а не «{p}». "
                                  "Если нужно удалить что-то другое — попроси пользователя.")
        return f(p, *a, **k)
    g.__name__ = name
    return g
os.remove = _wrap(os.remove, "remove"); os.unlink = _wrap(os.unlink, "unlink"); os.rmdir = _wrap(os.rmdir, "rmdir")
shutil.rmtree = _wrap(shutil.rmtree, "rmtree")
_pu = pathlib.Path.unlink
pathlib.Path.unlink = lambda self, *a, **k: (_wrap(lambda p, *a2, **k2: _pu(pathlib.Path(p), *a2, **k2), "unlink"))(self, *a, **k)
_pr = pathlib.Path.rmdir
pathlib.Path.rmdir = lambda self: (_wrap(lambda p: _pr(pathlib.Path(p)), "rmdir"))(self)
