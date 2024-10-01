from setuptools import setup
from setuptools import find_packages

package_name = 'uav_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],                           #<!--- this can be changed, depending on you desire----->
    #packages=find_packages(exclude=['test']),
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
            'vision_simulation_node = uav_py.vision_simulation:main',
            'video_stream_node = uav_py.video_stream:main',
            'test_detection_node = uav_py.test_detection:main',
            'environment_node = uav_py.environment:main',
            'aruco_single_tracker_node = uav_py.aruco_single_tracker:main',
        ],
    },
)
