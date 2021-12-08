from setuptools import setup, find_packages

from havi import __version__

setup(
    name="havi",
    version=__version__,
    description="perform bayesian inference over physical models",
    url="https://github.com/bjornaer/havi",
    download_url="https://github.com/bjornaer/havi/archive/refs/tags/v.0.0.2-alpha.tar.gz",
    author="Francisco Grings, Maximiliano Schulkin",
    author_email="max.schulkin@gmail.com",
    keywords = ['physics', 'scatering', 'bayesian', 'inference', 'data', 'science'],
    packages=find_packages(include=["havi"]),
    license="Apache2.0",
    install_requires=["numpy", "torch", "pyro-ppl", "pyro-api"],
    classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Scientific Community',
    'Topic :: Data Analysis :: Bayesian Inference',

    # Pick your license as you wish
    'License :: OSI Approved :: Apache 2 License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
  ],
)