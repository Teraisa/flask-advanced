import os
import sys
import tempfile
from typing import Any, AnyStr, Callable, ContextManager, IO, Iterator, Optional, Text

def replace_atomic(src: AnyStr, dst: AnyStr) -> None: ...
def move_atomic(src: AnyStr, dst: AnyStr) -> None: ...
class AtomicWriter(object):
    def __init__(self, path: AnyStr, mode: Text='w', overwrite: bool=False) -> None: ...
    def open(self) -> ContextManager[IO]: ...
    def _open(self, get_fileobject: Callable) -> ContextManager[IO]: ...
    def get_fileobject(self, dir: Optional[AnyStr] = None, **kwargs) -> IO: ...
    def sync(self, f: IO) -> None: ...
    def commit(self, f: IO) -> None: ...
    def rollback(self, f: IO) -> None: ...
def atomic_write(path: AnyStr, writer_cls: type=AtomicWriter, **cls_kwargs) -> ContextManager[IO]: ...