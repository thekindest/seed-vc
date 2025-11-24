from setuptools import setup, find_packages

setup(
    name="seed-vc",
    version="0.0.0",
    packages=find_packages(),
    py_modules=[
        "seed_vc_wrapper",
        "hf_utils",
        "optimizers",
    ],
    include_package_data=True,
)
