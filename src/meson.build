# Generate headers
version_str = ''.join(meson.project_version().split('.'))
lib_header_conf = configuration_data()
lib_header_conf.set('MAGIC_VERSION', version_str)
lib_header = configure_file(configuration: lib_header_conf, input: 'magic.h.in', output: 'magic.h')
conf_header = configure_file(configuration: conf, output: 'config.h')
install_headers(lib_header)

# Source files
libmagic_src = [
    'buffer.c', 'magic.c', 'apprentice.c', 'softmagic.c', 'ascmagic.c',
    'encoding.c', 'compress.c', 'is_csv.c', 'is_json.c', 'is_tar.c', 'readelf.c', 'print.c',
    'fsmagic.c', 'funcs.c', 'file.h', 'readelf.h', 'tar.h', 'apptype.c', 'der.c', 'der.h',
    'file_opts.h', 'elfclass.h', 'mygetopt.h', 'cdf.c', 'cdf_time.c', 'readcdf.c', 'cdf.h'
]
file_src = ['file.c', 'seccomp.c']
foreach func : repl_funcs
    if not conf.get('have_' + func, false)
        libmagic_src += func + '.c'
    endif
endforeach

# Build targets
c_args = '-DHAVE_CONFIG_H'
libmagic = library(
    'magic', libmagic_src, install: true, c_args: c_args,
    dependencies: [bz2_dep, zlib_dep, lzma_dep, seccomp_dep]
)
libmagic_dep = declare_dependency(include_directories: '.', link_with: libmagic)
file = executable('file', file_src, link_with: libmagic, install: true, c_args: c_args)
