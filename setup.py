from setuptools import setup, find_packages
import RaspiMotorHat

setup(
    name="RaspiMotorHat",
    version=RaspiMotorHat.__VERSION__,
    description='Raspberry Pi Motor Hat',
    url='https://github.com/Alictronix/Raspi-MotorHat',
    author='Alictronix',
    author_email='armjaz@gmail.com',
    install_requires=[
        'smbus',
        'evdev'
    ],
    packages=find_packages(),
    python_requires='>=3.5, <4',
)