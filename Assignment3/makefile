CARGO = cargo
CARGO = $(shell which cargo 2> /dev/null)
CARGO_V = $(shell ${CARGO} -V)
FLAGS = $(MAKEFLAGS)

all: clean build
	
clean:
	@rm -r -f target
	@printf "\e[33m   Cleaning up old builds...\e[0m (rm -r -f target)\n"

build: src/main.rs
	@printf "\e[34m   Compiling with\e[0m %s\n" "$(CARGO_V)"
	@$(CARGO) build -r