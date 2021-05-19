"""
Python - sys Module

The sys module provides information about constants, functions and methods of the Python interpreter.

>> dir(sys)
[‘__displayhook__’, ‘__doc__’, ‘__excepthook__’, ‘__interactivehook__’, ‘__loader__’, ‘__name__’, ‘__package__’,
‘__spec__’, ‘__stderr__’, ‘__stdin__’, ‘__stdout__’, ‘_clear_type_cache’, ‘_current_frames’, ‘_debugmallocstats’,
‘_getframe’, ‘_git’, ‘_home’, ‘_xoptions’,
‘abiflags’, ‘api_version’, ‘argv’, ‘base_exec_prefix’, ‘base_prefix’, ‘builtin_module_names’, ‘byteorder’,
‘call_tracing’, ‘callstats’, ‘copyright’, ‘displayhook’, ‘dont_write_bytecode’, ‘exc_info’, ‘excepthook’,
‘exec_prefix’, ‘executable’, ‘exit’, ‘flags’, ‘float_info’, ‘float_repr_style’, ‘get_asyncgen_hooks’,
‘get_coroutine_wrapper’, ‘getallocatedblocks’, ‘getcheckinterval’, ‘getdefaultencoding’, ‘getdlopenflags’,
‘getfilesystemencodeerrors’, ‘getfilesystemencoding’, ‘getprofile’, ‘getrecursionlimit’, ‘getrefcount’,
‘getsizeof’, ‘getswitchinterval’, ‘gettrace’, ‘hash_info’, ‘hexversion’, ‘implementation’, ‘int_info’,
‘intern’, ‘is_finalizing’, ‘maxsize’, ‘maxunicode’, ‘meta_path’, ‘modules’, ‘path’, ‘path_hooks’, ‘path_importer_cache’,
‘platform’, ‘prefix’, ‘ps1’, ‘ps2’, ‘set_asyncgen_hooks’, ‘set_coroutine_wrapper’, ‘setcheckinterval’, ‘setdlopenflags’,
‘setprofile’, ‘setrecursionlimit’, ‘setswitchinterval’, ‘settrace’, ‘stderr’, ‘stdin’, ‘stdout’, ‘thread_info’,
‘version’, ‘version_info’, ‘warnoptions’]

"""
import sys

# Get maximum recursion depth
print(sys.getrecursionlimit())

# Set maximum recursion depth
sys.setrecursionlimit(1100)
print(sys.getrecursionlimit())

# Current version of Python
print(sys.version)
print(sys.version_info)

# Standard output, standard input, standard error stream
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
# May be redirected to file

# Python executable file
print(sys.executable)

# Largest positive integer
print(sys.maxsize)

# The search path where python is looking for modules
print(sys.path)

# System platform
print(sys.platform)

# System float and int number info
print(sys.float_info)
print(sys.int_info)
