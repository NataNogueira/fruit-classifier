.PHONY: help install clean download-data train run test lint

PYTHON := python3
PIP := pip3
SRC_DIR := src
CONFIG_DIR := config
FRONTEND_DIR := frontend
MODEL_FILE := fruit_model.h5
DATA_DIR := data

help:
	@echo "Comandos disponíveis:"
	@echo "  make install         - Instala as dependências do projeto"
	@echo "  make download-data   - Baixa o dataset do Kaggle"
	@echo "  make train          - Treina o modelo"
	@echo "  make run            - Executa a aplicação Streamlit"
	@echo "  make lint           - Verifica o código com pylint e flake8"
	@echo "  make clean          - Remove arquivos temporários e dados"
	@echo "  make init           - Configuração inicial (install + download-data)"

install:
	@echo "Configurando ambiente virtual..."
	@if [ ! -d ".venv" ]; then \
		echo "Criando ambiente virtual..."; \
		python3 -m venv .venv; \
	fi
	@echo "Ativando ambiente virtual e instalando dependências..."
	@if [ -f requirements.txt ]; then \
		echo "Instalando dependências do requirements.txt..."; \
		. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; \
	else \
		echo "Arquivo requirements.txt não encontrado. Nenhuma dependência será instalada."; \
	fi

download-data:
	@echo "Baixando dataset do Kaggle..."
	$(PYTHON) -m src.download_data

train:
	@echo "Iniciando treinamento do modelo..."
	$(PYTHON) -m src.train

run:
	@echo "Iniciando aplicação Streamlit..."
	streamlit run app.py

lint:
	@echo "Verificando código com flake8..."
	@-flake8 $(SRC_DIR) $(CONFIG_DIR) $(FRONTEND_DIR) app.py --max-line-length=120 --exclude=__pycache__,*.pyc
	@echo "Verificando código com pylint..."
	@-pylint $(SRC_DIR) $(CONFIG_DIR) $(FRONTEND_DIR) app.py --disable=C0111,R0903


clean:
	@echo "Removendo arquivos temporários..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.log" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
	@echo "Removendo dados..."
	@rm -rf $(DATA_DIR)
	@echo "Removendo modelo treinado..."
	@rm -f $(MODEL_FILE)
	@echo "Limpeza completa realizada!"

init: install download-data
	@echo "Setup inicial concluído!"
	@echo "Execute 'make train' para treinar o modelo."
	@echo "Execute 'make run' para iniciar a aplicação."
