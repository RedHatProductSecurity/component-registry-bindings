############################################################################
# defaults
############################################################################
openapi-python-client=`which openapi-python-client`
pc=`which pip-compile`
ps=`which pip-sync`
package_dir=component_registry_bindings/
bindings_dir=$(package_dir)bindings/


############################################################################
# client generation
############################################################################
update:
	@echo "Updating bindings python client"
	cd $(package_dir) \
	&& $(openapi-python-client) update --path openapi_schema.yml \
	--config $(shell pwd)/$(package_dir)bindings_config.yml \
	--custom-template-path templates
	touch $(bindings_dir)__init__.py

create:
	@echo "Creating bindings python client"
	cd $(package_dir) \
	&& $(openapi-python-client) generate --path openapi_schema.yml \
	--config $(shell pwd)/$(package_dir)bindings_config.yml \
	--custom-template-path templates
	touch $(bindings_dir)__init__.py

############################################################################
# dev entrypoints
############################################################################
compile-deps:
	@echo ">compiling python dependencies"
	$(pc) --generate-hashes --allow-unsafe requirements.in
	$(pc) --generate-hashes --allow-unsafe devel-requirements.in
	[ -f local-requirements.in ] && $(pc) --generate-hashes --allow-unsafe local-requirements.in || true

sync-deps:
	@echo ">synchronizing python dependencies"
	$(ps) requirements.txt devel-requirements.txt $$([ -f local-requirements.txt ] && echo 'local-requirements.txt')
