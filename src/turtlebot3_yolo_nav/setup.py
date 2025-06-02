from setuptools import setup

package_name = 'turtlebot3_yolo_nav'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name + '/launch', ['launch/yolo_nav.launch.py']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user3',
    maintainer_email='user3@example.com',
    description='YOLO + Navigation integration for TurtleBot3',
    license='MIT',
    entry_points={
        'console_scripts': [
            'yolo_node = turtlebot3_yolo_nav.yolo_node:main',
            'nav_node = turtlebot3_yolo_nav.nav_node:main',
        ],
    },
)
