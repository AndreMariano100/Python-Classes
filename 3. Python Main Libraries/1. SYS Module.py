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

# 1. System error
sys.stderr.write('This is certainly an error\n')
# sys.stderr.flush()

# # 2. System output
# sys.stdout.write('This is a regular printed message\n')
#
# 3. Argv
# print(sys.argv)
#
#
# if len(sys.argv) > 1:
#     print(sys.argv[1])

# ['C:/Users/csm0/PycharmProjects/PythonClasses/3. Python Main Libraries/1. SYS Module.py']
# May be used to communicate with other languages
# It will show all the arguments used to call the function
# Try calling the function like:
#   python "1. SYS Module.py"
#   python "1. SYS Module.py" "extra argument"
#   python "1. SYS Module.py" "[0, 1, 2, 3, 4, 5]"
#
# # 4. Get maximum recursion depth
# print(sys.getrecursionlimit())
#
# # 5. Set maximum recursion depth
# sys.setrecursionlimit(1100)
# print(sys.getrecursionlimit())

# # 6. Current version of Python
# print(sys.version)
# print(sys.version_info)
# """
# 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# sys.version_info(major=3, minor=9, micro=2, releaselevel='final', serial=0)
# """
#
# # 7. Python executable file
# print(sys.executable)
#
# # 8. Largest positive integer: 9223372036854775807
# print(sys.maxsize)
#
# # 9. The search path where python is looking for modules
# print(sys.path)
# """
# ['C:\\Users\\csm0\\PycharmProjects\\PythonClasses\\3. Python Main Libraries',
# 'C:\\Users\\csm0\\PycharmProjects\\PythonClasses',
# 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\python39.zip',
# 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\DLLs',
# 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib',
# 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391',
# 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv',
# 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv\\lib\\site-packages',
# 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv\\lib\\site-packages\\win32',
# 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv\\lib\\site-packages\\win32\\lib',
# 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv\\lib\\site-packages\\Pythonwin']
# """
# #
# # 10. System platform: win32
# print(sys.platform)
# #
# # # 11. System float and int number info
# # print(sys.float_info)
# # print(sys.int_info)
# """
# sys.float_info
# (max=1.7976931348623157e+308,
# max_exp=1024,
# max_10_exp=308,
# min=2.2250738585072014e-308,
# min_exp=-1021,
# min_10_exp=-307,
# dig=15,
# mant_dig=53,
# epsilon=2.220446049250313e-16,
# radix=2,
# rounds=1)
#
# sys.int_info(bits_per_digit=30, sizeof_digit=4)
# """
#
# # 12. Copyright
# # print(sys.copyright)
# """
# Copyright (c) 2001-2021 Python Software Foundation.
# All Rights Reserved.
#
# Copyright (c) 2000 BeOpen.com.
# All Rights Reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All Rights Reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
# All Rights Reserved.
# """
#
# # 13. Get Size Off (bytes)
# a = 15
# b = 15.0
# c = 'fifteen'
# d = ['list', a, b, c]
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))

# 14. Built in module names
# print(sys.builtin_module_names)
"""
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', 
'_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', 
'_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_peg_parser', '_pickle', 
'_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', 
'_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 

'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 
'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')

"""
# # 15. Modules
# print(sys.modules)
"""
{'sys': <module 'sys' (built-in)>, 
'builtins': <module 'builtins' (built-in)>, 
'_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, 
'_imp': <module '_imp' (built-in)>, 
'_thread': <module '_thread' (built-in)>, 
'_warnings': <module '_warnings' (built-in)>, 
'_weakref': <module '_weakref' (built-in)>, 
'_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, 
'nt': <module 'nt' (built-in)>,
'_io': <module 'io' (built-in)>, 
'marshal': <module 'marshal' (built-in)>, 
'winreg': <module 'winreg' (built-in)>, 
'time': <module 'time' (built-in)>, 
'zipimport': <module 'zipimport' (frozen)>, 
'_codecs': <module '_codecs' (built-in)>, 
'codecs': <module 'codecs' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\codecs.py'>, 
'encodings.aliases': <module 'encodings.aliases' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\encodings\\aliases.py'>, 'encodings': <module 'encodings' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\encodings\\__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\encodings\\utf_8.py'>, '_signal': <module '_signal' (built-in)>, 'encodings.latin_1': <module 'encodings.latin_1' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\encodings\\latin_1.py'>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\abc.py'>, 'io': <module 'io' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\io.py'>, '__main__': <module '__main__' from 'C:\\Users\\csm0\\PycharmProjects\\PythonClasses\\3. Python Main Libraries\\1. SYS Module.py'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\stat.py'>, '_collections_abc': <module '_collections_abc' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\_collections_abc.py'>, 'genericpath': <module 'genericpath' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\genericpath.py'>, 'ntpath': <module 'ntpath' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\ntpath.py'>, 'os.path': <module 'ntpath' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\ntpath.py'>, 'os': <module 'os' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\os.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\_sitebuiltins.py'>, '_locale': <module '_locale' (built-in)>, '_bootlocale': <module '_bootlocale' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\_bootlocale.py'>, 'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\encodings\\cp1252.py'>, 'types': <module 'types' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\types.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\warnings.py'>, 'importlib': <module 'importlib' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\importlib\\__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\importlib\\machinery.py'>, '_heapq': <module '_heapq' (built-in)>, 'heapq': <module 'heapq' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\heapq.py'>, 'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\keyword.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\operator.py'>, 'reprlib': <module 'reprlib' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\collections\\__init__.py'>, 'collections.abc': <module 'collections.abc' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\collections\\abc.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\functools.py'>, 'contextlib': <module 'contextlib' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\contextlib.py'>, 'enum': <module 'enum' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\enum.py'>, '_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\sre_constants.py'>, 'sre_parse': <module 'sre_parse' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\sre_parse.py'>, 'sre_compile': <module 'sre_compile' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\sre_compile.py'>, 'copyreg': <module 'copyreg' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\copyreg.py'>, 're': <module 're' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\re.py'>, 
'typing.io': <class 'typing.io'>, 
'typing.re': <class 'typing.re'>, 
'typing': <module 'typing' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\typing.py'>, 
'importlib.abc': <module 'importlib.abc' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\importlib\\abc.py'>, 'importlib.util': <module 'importlib.util' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\importlib\\util.py'>, 'mpl_toolkits': <module 'mpl_toolkits' (namespace)>, 'pywin32_bootstrap': <module 'pywin32_bootstrap' from 'C:\\Users\\csm0\\PycharmProjects\\BasicEnvironment\\venv\\lib\\site-packages\\win32\\lib\\pywin32_bootstrap.py'>, 'site': <module 'site' from 'C:\\Users\\csm0\\Documents\\3. Python\\0. Programas\\Python391\\lib\\site.py'>}

"""
