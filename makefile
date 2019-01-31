VERSION := $(shell python -c "import easydarkfigs; print(easydarkfigs.__version__)")

install:
	pip install . --upgrade

upload: install
	python setup.py sdist bdist_wheel
	twine upload dist/easydarkfigs-$(VERSION)*
