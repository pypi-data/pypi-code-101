#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages, Extension
import os
from os.path import join as pjoin
from Cython.Distutils import build_ext


# os.system('nvcc -Xcompiler -fPIC -shared -o pydpm/_sampler/_compact/sampler_kernel.so pydpm/_sampler/_compact/sampler_kernel.cu')  # useless


c_package_data=[
    'pydpm/_sampler/_compact/crt_cpu.dll',
    'pydpm/_sampler/_compact/crt_multi_aug_cpu.dll',
    'pydpm/_sampler/_compact/multi_aug_cpu.dll',
    'pydpm/_sampler/_compact/sampler_kernel.cu',
    'pydpm/_sampler/_compact/sampler_kernel.h',
]


def find_in_path(name, path):
    "Find a file in a search path"
    #adapted fom http://code.activestate.com/recipes/52224-find-a-file-given-a-search-path/
    for dir in path.split(os.pathsep):
        binpath = pjoin(dir, name)
        if os.path.exists(binpath):
            return os.path.abspath(binpath)
    return None
def locate_cuda():
    """Locate the CUDA environment on the system
    Returns a dict with keys 'home', 'nvcc', 'include', and 'lib64'
    and values giving the absolute path to each directory.
    Starts by looking for the CUDAHOME env variable. If not found, everything
    is based on finding 'nvcc' in the PATH.
    """

    # first check if the CUDAHOME env variable is in use
    if 'CUDAHOME' in os.environ:
        home = os.environ['CUDAHOME']
        nvcc = pjoin(home, 'bin', 'nvcc')
    else:
        # otherwise, search the PATH for NVCC
        default_path = pjoin(os.sep, 'usr', 'local', 'cuda', 'bin')
        nvcc = find_in_path('nvcc', os.environ['PATH'] + os.pathsep + default_path)
        if nvcc is None:
            raise EnvironmentError('The nvcc binary could not be '
                'located in your $PATH. Either add it to your path, or set $CUDAHOME')
        home = os.path.dirname(os.path.dirname(nvcc))

    cudaconfig = {'home':home, 'nvcc':nvcc,
                  'include': pjoin(home, 'include'),
                  'lib64': pjoin(home, 'lib64')}
    for k, v in cudaconfig.items():
        if not os.path.exists(v):
            raise EnvironmentError('The CUDA %s path could not be located in %s' % (k, v))

    return cudaconfig
CUDA = locate_cuda()


# =========================
def customize_compiler_for_nvcc(self):
    """inject deep into distutils to customize how the dispatch
    to gcc/nvcc works.
    If you subclass UnixCCompiler, it's not trivial to get your subclass
    injected in, and still have the right customizations (i.e.
    distutils.sysconfig.customize_compiler) run on it. So instead of going
    the OO route, I have this. Note, it's kindof like a wierd functional
    subclassing going on."""
 
    # tell the compiler it can processes .cu
    self.src_extensions.append('.cu')
 
    # save references to the default compiler_so and _comple methods
    default_compiler_so = self.compiler_so
    super = self._compile
 
    # now redefine the _compile method. This gets executed for each
    # object but distutils doesn't have the ability to change compilers
    # based on source extension: we add it.
    def _compile(obj, src, ext, cc_args, extra_postargs, pp_opts):
        print(extra_postargs)
        if os.path.splitext(src)[1] == '.cu':
            # use the cuda for .cu files
            self.set_executable('compiler_so', CUDA['nvcc'])
            # use only a subset of the extra_postargs, which are 1-1 translated
            # from the extra_compile_args in the Extension class
            postargs = extra_postargs['nvcc']
        else:
            postargs = extra_postargs['gcc']
 
        super(obj, src, ext, cc_args, postargs, pp_opts)
        # reset the default compiler_so, which we might have changed for cuda
        self.compiler_so = default_compiler_so
 
    # inject our redefined _compile method into the class
    self._compile = _compile
# run the customize_compiler
class custom_build_ext(build_ext):
    def build_extensions(self):
        customize_compiler_for_nvcc(self.compiler)
        build_ext.build_extensions(self)



setup(
    name='pydpmtest',
    version='0.2.0',
    description='A python library focuses on constructing deep probabilistic models on GPU.',
    py_modules=['pydpm'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=['Chaojie Wang', 'Wei Zhao', 'Jiawen Wu'],
    author_email='xd_silly@163.com',
    maintainer='BoChenGroup',
    license='Apache License Version 2.0',
    packages=find_packages(),
    package_data={'pydpm': c_package_data},
    data_files=c_package_data,
    platforms=["Windows", "Linux"],
    url='https://github.com/BoChenGroup/Pydpm',
    requires=['numpy', 'scipy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: GPU :: NVIDIA CUDA',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    # ext_modules=[
    #     Extension('pydpm._sampler._compact.sampler_kernel',
    #         sources=['pydpm/_sampler/_compact/sampler_kernel.cu'],
    #         library_dirs=[CUDA['lib64']],
    #         # libraries=['cuda_runtime.h', 'device_launch_parameters.h', 'curand.h', 'curand_kernel.h', 'stdlib.h', 'stdio.h'],
    #         extra_compile_args={'nvcc': ['-arch=sm_52',
    #                                  '--ptxas-options=-v',
    #                                  '-c',
    #                                  '--compiler-options',
    #                                  "'-fPIC'"]},  # nvcc -Xcompiler -fPIC -shared -o
    #         include_dirs=['pydpm/_sampler/_compact/', CUDA['include']], # 头文件
    #     )
    # ],
    cmdclass={'build_ext': custom_build_ext},
)
