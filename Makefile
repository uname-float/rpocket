.ONESHELL:
.PHONY: help run test lint format clean install update setup setup-project check all build

# Visualizza l'help
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  run             Avvia l'applicazione"
	@echo "  test            Esegui i test"
	@echo "  lint            Esegui il linter"
	@echo "  format          Esegui la formattazione del codice"
	@echo "  clean           Pulisci i file generati"
	@echo "  install         Installa le dipendenze"
	@echo "  update          Aggiorna le dipendenze"
	@echo "  setup           Esegui il setup dell'ambiente virtuale"
	@echo "  setup-project   Esegui il setup iniziale del progetto"
	@echo "  check           Esegui tutte le verifiche (lint e test)"
	@echo "  all             Esegui tutte le operazioni di formattazione e verifica"
	@echo "  build           Esegui la build del pacchetto"

# Avvia l'applicazione con suggerimento per gli argomenti
.PHONY: run
run:
	@echo "Usage: make run COMMAND [ARGS...]"
	@echo ""
	@echo "Commands:"
	@echo "  add-credit-card    Aggiunge una carta di credito"
	@echo ""
	@echo "Esempio:"
	@echo "  make run add-credit-card 1234567812345678 2024-12-31 'Mario Rossi' 123 'Carta di credito principale'"
	@poetry run rpocket/cli.py add-credit-card \
		1234567812345678 \
        2024-12-31 \
    	"Mario Rossi" \
        123 \
        "Carta di credito principale"

# Comando per eseguire i test
.PHONY: test
test:
	poetry run pytest

# Definizione del target test con esecuzione dei test
# generazione e visualizzazione dei file di coverage
.PHONY: coverage-test
coverage-test: ## Run tests and display coverage report.
	poetry run pytest -v --cov-config .coveragerc --cov=rpocket -l --tb=short --maxfail=1 tests/
	coverage xml
	coverage html

# Comando per eseguire il linter
.PHONY: lint
lint:
	poetry run flake8 rpocket/
	poetry run black -l 79 rpocket/
	poetry run black -l 79  tests/
	poetry run mypy --ignore-missing-imports rpocket/

# Comando per eseguire la pulizia dei file generati
.PHONY: clean
clean:
	rm -rf dist build *.egg-info

# Comando per eseguire l'installazione delle dipendenze
.PHONY: install
install:
	poetry install

# Comando per eseguire l'aggiornamento delle dipendenze
.PHONY: update
update:
	poetry update

# Comando per eseguire il setup dell'ambiente virtuale
.PHONY: setup
setup:
	poetry env use python3.9

# Comando per eseguire il setup iniziale del progetto
.PHONY: setup-project
setup-project: setup install

# Comando per eseguire tutte le verifiche
.PHONY: check
check: lint test

# Comando per eseguire tutte le operazioni di formattazione e verifica
.PHONY: all
all: format check

# Comando per eseguire la build del pacchetto
.PHONY: build
build:
	poetry build
