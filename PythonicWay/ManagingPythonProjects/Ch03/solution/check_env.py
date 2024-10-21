def check_version(name, version_prefix):
    mod = __import__(name)
    version = mod.__version__
    assert version.startswith(version_prefix), \
        f'{name} version is {version} (wanted {version_prefix})'


# Production packages
check_version('flask', '1.1')
check_version('flask_login', '0.4.1')
check_version('numpy', '1.16.4')

# Development packages
check_version('flake8', '3.7')
check_version('pytest', '5.1.1')
check_version('pytest_benchmark', '3.2.2')
