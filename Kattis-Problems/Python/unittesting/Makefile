PLANTUML = java -jar ~/Desktop/plantuml.jar
DOCS = docs

all: static_type_check testin create_docs create_uml run_test_main

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	mkdir -p docs
	pdoc -o docs --html unittesting.py --force
	pdoc -o docs --html main.py --force
	pdoc --force -o docs main.py unittesting.py 


static_type_check:
ifeq ($(shell which mypy), )
	@echo "mypy not found. Downloading..."
	pip install mypy
endif
	@mypy --strict --disallow-untyped-defs unittesting.py
	@mypy --strict --disallow-untyped-defs main.py
	@echo "Type Checking Passed... "

run: 
	@python main.py

onetest:
	@cat data/m0000.in | python main.py

datatest:
	
	@cat data/m0000.in | python main.py
	@cat data/m0001.in | python main.py
	@cat data/m0002.in | python main.py
	@cat data/m0003.in | python main.py
	@cat data/m0004.in | python main.py
	@cat data/m0005.in | python main.py

testin:
	@cat data/m0000.in | python main.py | diff - data/m0000.ans
	@cat data/m0001.in | python main.py | diff - data/m0001.ans
	@cat data/m0002.in | python main.py | diff - data/m0002.ans
	@cat data/m0003.in | python main.py | diff - data/m0003.ans
	@cat data/m0004.in | python main.py | diff - data/m0004.ans
	@cat data/m0005.in | python main.py | diff - data/m0005.ans

	@echo "Kattis test passed!"

create_uml: create_doc_folder
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "~/plantuml.jar not found. Downloading...."
	curl -L -o ~/Desktop/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

endif
	@echo "~/Desktop/plantuml.jar FOUND! Creating pngs..."
	$(PLANTUML) uml/unittesting.plantuml
	$(PLANTUML) uml/main.plantuml

run_test_main:
	$ pytest
	