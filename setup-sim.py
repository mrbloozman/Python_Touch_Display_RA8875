from setuptools import setup
setup(
    name="Touch_Display_RA8875_sim",
    version="0.1.2",
    packages=['touch_display_ra8875_sim'],
    # scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['adafruit_ra8875_sim>=0.1'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Mark Schwartz",
    author_email="mrbloozman@gmail.com",
    description="Application framework including input controls, touch event handling, etc, to assist in running RA8875 via spi on NTC CHIP",
    license="MIT",
    # keywords="hello world example examples",
    # url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        # "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        # "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://www.github.com/mrbloozman/Python_Touch_Display_RA8875",
    }

    # could also include long_description, download_url, classifiers, etc.
)