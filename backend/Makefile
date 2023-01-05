# This is the default target, which will be built when 
# you invoke make
.PHONY: build
build:
	pnpm install
	pnpm run package
	mkdir -p ../bin
	mv ./out/server ../bin/server

# This rule tells make to delete hello and hello.o
.PHONY: clean 
clean:
	rm -f ./out/bundle.js
	rm -f ./out/server
