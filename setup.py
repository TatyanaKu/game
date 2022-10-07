from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Tanya K',
    author_email='tanyaku2801@gmail.com',
    description = 'FastApi app',
    install_requires=[
        'fastapi=='0.85.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0',
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)
