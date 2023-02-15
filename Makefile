PROJECT=fake-it-til-you-make-it-mocks
PYTESTOPTS?=
PYTHON_VERSION?=3.10.0

.PHONY: pyenv
pyenv:
	pyenv install ${PYTHON_VERSION} --skip-existing
	pyenv uninstall ${PROJECT} || true
	pyenv virtualenv ${PYTHON_VERSION} ${PROJECT}
	pyenv local ${PROJECT}
	pip install black pytest pdbpp poetry
	sed -i '/export VIRTUAL_ENV=/d' .envrc || true
	echo "export VIRTUAL_ENV=\$$$\(pyenv prefix)" >> .envrc
	direnv allow || true

.PHONY: all
all:

.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest \
	    --verbose \
	    --tb=short \
	    ${PYTESTOPTS}

.PHONY: render
render:
	quarto render ${PROJECT}.qmd

.PHONY: publish
publish:
	quarto publish quarto-pub ${PROJECT}.qmd

.PHONY: clean
clean:
	find . \( -name '*.pyc' -or -name '*.pyo' \) -print -delete
	find . -name '__pycache__' -print -delete

.PHONY: distclean
distclean:
	rm -rf dist ${PROJECT}.html ${PROJECT}_files
