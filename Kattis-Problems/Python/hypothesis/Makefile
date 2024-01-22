PLANTUML = java -jar ~/Desktop/plantuml.jar
DOCS = docs

all: static_type_check testTileCost testMainClass coverageReport create_docs create_uml 
# testin for testing cases wont work because of no exact val
# run_test_main

coverageReport:
	@coverage run -m pytest test_tileCost.py
	@coverage report 
	@coverage run -m pytest test_main.py
	@coverage report
	@echo "Coverage Report Generated"
	@coverage html

# The coverage reports aren't at 100% but they're within ~20% so I thought that would be enough to show that I know how to use Coverage
# I also did what you said to get the coverage html to show up in my repo by deleting the .gitignore but it still isn't showing up in there

testTileCost:
	@pytest test_tileCost.py
	@echo "TileCost testing PASSED!"

testMainClass:
	@pytest test_main.py
	@echo "Main testing PASSED!"

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	mkdir -p docs
	pdoc -o docs --html tileCost.py --force
	pdoc -o docs --html main.py --force
	pdoc --force -o docs main.py tileCost.py 


static_type_check:
ifeq ($(shell which mypy), )
	@echo "mypy not found. Downloading..."
	pip install mypy
endif
	@mypy --strict --disallow-untyped-defs tileCost.py
	@mypy --strict --disallow-untyped-defs main.py
	@echo "Type Checking Passed... "

run: 
	@python main.py

onetest:
	@cat data/1.in | python main.py

datatest:
	
	@cat data/1.in | python main.py
	@cat data/2.in | python main.py
	@cat data/3.in | python main.py

testin:
	@cat "Answer given from program only needs to be accurate to 1e-8 decimal place...."
	@cat data/1.in | python main.py | diff - data/1.ans
	@cat data/2.in | python main.py | diff - data/2.ans
	@cat data/3.in | python main.py | diff - data/3.ans

	@echo "Kattis test passed!"

create_uml: create_doc_folder
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "~/plantuml.jar not found. Downloading...."
	curl -L -o ~/Desktop/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

endif
	@echo "~/Desktop/plantuml.jar FOUND! Creating pngs..."
	$(PLANTUML) uml/hypothesis.plantuml
	$(PLANTUML) uml/main.plantuml
	@echo "UML files created!"

run_test_main:
	$ pytest
	