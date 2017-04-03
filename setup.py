from setuptools import setup

setup(
    name='countbyalexa',
    version='0.0.1',
    url='https://github.com/ravishan16/countbyalexa',
    license='MIT',
    author='Ravishankar Sivasubramaniam',
    author_email='ravi_siva@live.com',
    description='Alexa Skill to Count By',
    packages=['countbyalexa'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'falsk-ask',
        'zappa',
        'awscli',
        'pylint',
        'nose'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
