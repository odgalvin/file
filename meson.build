project('file', 'c',
        meson_version: '>= 0.56',
        license: 'BSD-2-Clause',
        version: '5.40',
	default_options: ['b_ndebug=if-release'])

cc = meson.get_compiler('c')
pkg = import('pkgconfig')
pkgdatadir = get_option('prefix') / get_option('datadir') / 'misc'
custom_magic_dir = pkgdatadir / 'magic'

# Dependencies
m_dep = cc.find_library('m', required: false)
bz2_dep = cc.find_library('bz2', required: get_option('bzlib'))
zlib_dep = dependency('zlib', required: get_option('zlib'))
lzma_dep = dependency('liblzma', required: get_option('xzlib'))
seccomp_dep = dependency('libseccomp', required: get_option('libseccomp'))

# Checks
headers = [
    'stdint.h', 'fcntl.h', 'inttypes.h', 'unistd.h', 'utime.h', 'wchar.h',
    'wctype.h', 'getopt.h', 'err.h', 'xlocale.h', 'sys/mman.h', 'sys/stat.h',
    'sys/types.h', 'sys/utime.h', 'sys/time.h', 'sys/sysmacros.h',
    'sys/wait.h', 'zlib.h', 'bzlib.h', 'lzma.h'
]
funcs = [
    'strndup', 'mkstemp', 'mkostemp', 'utimes', 'utime', 'wcwidth', 'strtof',
    'newlocale', 'uselocale', 'freelocale', 'memmem', 'pipe2', 'mmap', 'fork',
    'mbrtowc'
]
repl_funcs = [
    'getopt_long', 'asprintf', 'vasprintf', 'strlcpy', 'strlcat', 'getline',
    'ctime_r', 'asctime_r', 'localtime_r', 'gmtime_r', 'pread', 'strcasestr',
    'fmtcheck', 'dprintf'
]
conf = configuration_data()
conf.set('_GNU_SOURCE', true)
conf.set_quoted('MAGIC', custom_magic_dir)
conf.set_quoted('VERSION', meson.project_version())
foreach header : headers
    if cc.has_header(header)
        conf.set('HAVE_' + header.underscorify().to_upper(), 1)
    endif
endforeach
foreach func : funcs + repl_funcs
    if cc.has_function(func)
        conf.set('HAVE_' + func.underscorify().to_upper(), 1)
    endif
endforeach
conf.set10('BUILTIN_ELF', get_option('elf').enabled())
conf.set10('ELFCORE', get_option('elf-core').enabled())

# Directories
subdir('src')
subdir('magic')
#subdir('man')

# pkg-config file
pkg.generate(
    libmagic,
    name: 'libmagic',
    url: 'https://www.darwinsys.com/file/',
    description: 'An implementation of the Unix File(1) command.'
)
