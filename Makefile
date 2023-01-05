deckip := 192.168.0.128
deckport := 22
deckkey := $(-i $HOME/.ssh/id_rsa_steamdeck)
deckdir := /home/deck
deckpass := "sdeck"
workspaceBaseFolder := $(shell pwd)

createfolders:
	ssh deck@$(deckip) -p $(deckport) $(deckkey) 'mkdir -p $(deckdir)/homebrew/pluginloader && mkdir -p $(deckdir)/homebrew/plugins'

deploy:
	rsync -azp --delete \
		--rsh='ssh -p $(deckport) $(deckkey)' --exclude='.git/' \
		--exclude='.github/' --exclude='.vscode/' --exclude='node_modules/' \
		--exclude='src/' --exclude='*.log' \
		--exclude='.gitignore' . deck@$(deckip):$(deckdir)/homebrew/plugins/ftp-server

chmodfolders:
	ssh deck@$(deckip) -p $(deckport) $(deckkey) 'echo $(kkjdeckpass) | sudo -S chmod -R ug+rw $(deckdir)/homebrew/'

clean:
	rm -f ./backend/out/bundle.js
	rm -rf ./bin
	rm -rf ./dist/*
