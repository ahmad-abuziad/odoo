include .env
export

run/odoo:
	./odoo-bin -u lunch --without-demo=all  --addons-path=addons -d ${ODOO_DB} -r ${ODOO_DB_USERNAME} -w ${ODOO_DB_PASSWORD}