VERSION=`python setup.py --version`

default:
	@echo "Specify one of: serve, publish_docs, publish_package"

env:
	rm -Rf .env 
	virtualenv .env

serve:
	.env/bin/mkdocs serve -s -a 0.0.0.0:8000

publish_docs:
	.env/bin/mkdocs gh-deploy

publish_package:
	@echo Build python distribution
	python setup.py sdist bdist_wheel
	@echo "Publish to PyPI at https://pypi.python.org/pypi/rtd-dropdown"
	@echo "Run this manually: .env/bin/twine upload dist/mkdocs-rtd-dropdown-$(VERSION).tar.gz dist/mkdocs_rtd_dropdown-$(VERSION)-py2-none-any.whl"
