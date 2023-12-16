###################
## Build Targets ##
###################

.themes:
	mkdir -p .themes/

.themes/graymill: .themes
	git clone https://github.com/rn4ir/graymill.git .theme

build: .themes/graymill
	pelican

#########################
## Development Targets ##
#########################

local:
	pelican -lr