from setuptools import setup, find_packages


setup(
    name='django-collage',
    version="1.0",
    description='',
    keywords="django collage",
    long_description=open('README.rst').read(),
    author="GoTLiuM InSPiRiT",
    author_email='gotlium@gmail.com',
    url='http://github.com/gotlium/django-collage',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    install_requires=['setuptools', 'django', 'sorl-thumbnail', 'PIL'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
