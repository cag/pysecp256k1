from distutils.command.build import build
from setuptools import setup, find_packages
from subprocess import call
import requests


class BitcoinSecpBuild(build):

    def run(self):
        bitcoin_secp256k1 = "https://github.com/bitcoin/secp256k1/tarball/master"
        print("downloading tarball from " + bitcoin_secp256k1 + "...")
        r = requests.get(bitcoin_secp256k1)
        if r.status_code == 200:
            open('secp256k1.tar.gz', 'wb').write(r.content)
            call("./build.sh", shell=True)
        else:
            print("something went wrong while downloading " + bitcoin_secp256k1)
            print(r.status_code)



setup(
    name="secp256k1",
    version='0.0.1',
    description="secp256k1 wrapped with cffi to use with python",
    author="Jacob Stenum Czepluch",
    author_email="j.czepluch@gmail.com",
    url="https://github.com/czepluch/pysecp256k1",
    license="MIT",
    packages=find_packages(exclude=["_cffi_build", "_cffi_build/*"]),
    build_requires=["requests>=2.8.0"],
    install_requires=["cffi>=1.2.1"],
    setup_requires=["cffi>=1.2.1"],
    cffi_modules=["_cffi_build/secp256k1_build.py:ffi"],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    zip_safe=False,
    cmdclass={
        'build': BitcoinSecpBuild,
    }
)
