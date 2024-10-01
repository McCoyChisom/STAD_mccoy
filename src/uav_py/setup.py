from setuptools import setup
from setuptools import find_packages

package_name = 'uav_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ThankGodChisomWIlliams',
    maintainer_email='tgwilliamsc@gmail.com',
    description='UAV Python Package ROS2',
    license='Apache Licence 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_simulation = uav_py.vision_simulation:main',
            'stream = uav_py.video_stream:main',
            'detection = uav_py.test_detection:main',
            'environment = uav_py.environment:main',
            'follow_me = uav_py.aruco_single_tracker:main',
        ],
    },
)
