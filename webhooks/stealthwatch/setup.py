from setuptools import setup, find_packages

version = '0.1.0'

setup(
        name='alerta_stealthwatch',
        version=version,
        description='Alerta webhook for stealthwatch',
        url='',
        license='',
        author='Francis Begyn',
        author_email='francis.begyn@axians.com',
        packages=find_packages(),
        py_modules=['alerta_stealthwatch'],
        install_requirements=[''],
        include_package_data=True,
        zip_safe=True,
        entry_points={
            'alerta.webhooks': [
                    'stealthwatch = alerta_stealthwatch:StealthwatchWebhook'
                ]
            }
        )
