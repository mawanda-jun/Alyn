""" Setup script for installing Alyn """

from setuptools import setup

setup(
	name="alyn",
	version="0.1.3",
	author="Giovanni Cavallin",
	description="Fix skew in images",
	author_email="giovanni.cavallin@outlook.com",
	url='https://github.com/mawanda-jun/Alyn',
	download_url='https://github.com/mawanda-jun/Alyn.git',
	keywords=['image-processing', 'image-deskew', 'deskew', 'rotate', 'text'],
	packages=['alyn'],
	classifiers=[],
	license='MIT',
	install_requires=['numpy', 'scikit-image', 'scipy', 'matplotlib']
)
