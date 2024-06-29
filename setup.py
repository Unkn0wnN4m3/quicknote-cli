from setuptools import setup, find_packages

setup(
    name="pynote",
    author="Unk0wnN4m3",
    author_email="87839850+Unkn0wnN4m3@users.noreply.github.com",
    url="https://github.com/Unkn0wnN4m3/quicknote-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pynote = pynote:cli",
        ],
    },
    keywords=["cli", "python-cli", "notes", "click"],
)
