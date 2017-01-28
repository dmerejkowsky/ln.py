from setuptools import setup

setup(name="ln.py",
      version="0.1",
      description="symlinks made easier",
      url="https://github.com/dmerejkowsky/ln.py",
      author="Dimitri Merejkowsky",
      author_email="d.merej@gmail.com",
      entry_points={
        "console_scripts": [
          "lnp = ln:main",
        ]
      }
)
