clvsol_odoo_clvhealth_jcafb
===========================

* ubun14

    ::

        cd '/opt/openerp/jcafb'
        gzip -d clvhealth_jcafb_pro_2015-08-22a.sql.gz
        dropdb -i clvhealth_jcafb_dev -U postgres
        createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev -U postgres
        psql -f clvhealth_jcafb_pro_2015-08-22a.sql -d clvhealth_jcafb_dev -h localhost -p 5432 -q -U postgres

        cd '/opt/openerp/jcafb'
        pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev.sql
        mv clvhealth_jcafb_dev.sql clvhealth_jcafb_dev_2015-08-22a.sql
        gzip clvhealth_jcafb_dev_2015-08-22a.sql

    ::

        cd '/opt/openerp/jcafb'
        dropdb -i clvhealth_jcafb_dev -U postgres
        createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev -U postgres
        psql -f clvhealth_jcafb_dev_2015-08-22a.sql -d clvhealth_jcafb_dev -h localhost -p 5432 -q -U postgres

    ::

        cd cd '/opt/openerp/clvsol_odoo_clvhealth_jcafb/project'
        python install.py

* clvhealh-jcafb-2016-pro

    ::
        
        git clone https://github.com/CLVsol/odoo_addons /opt/openerp/clvsol_odoo_addons --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_l10n_br /opt/openerp/clvsol_odoo_addons_l10n_br --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_l10n_br

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_jcafb /opt/openerp/clvsol_odoo_addons_jcafb --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_jcafb

    ::

        cd '/opt/openerp/jcafb'
        gzip -d clvhealth_jcafb_dev_2015-11-02a.sql.gz
        su postgres
        dropdb -i clvhealth_jcafb_pro
        createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_pro
        psql -f clvhealth_jcafb_dev_2015-11-02a.sql -d clvhealth_jcafb_pro -h localhost -p 5432 -q
        exit

    ::

        cd '/opt/openerp/jcafb'
        pg_dump clvhealth_jcafb_pro -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_pro.sql
        mv clvhealth_jcafb_pro.sql clvhealth_jcafb_dev_2015-11-02a.sql
        gzip clvhealth_jcafb_dev_2015-11-02a.sql

    ::
        
        cd /opt/openerp/odoo
        su openerp
        ./openerp-server -c openerp-server-man.conf

* tkl-lamp-odoo-jcafb-tst

    ::
        
        git clone https://github.com/CLVsol/odoo_addons /opt/openerp/clvsol_odoo_addons --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_l10n_br /opt/openerp/clvsol_odoo_addons_l10n_br --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_l10n_br

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_jcafb /opt/openerp/clvsol_odoo_addons_jcafb --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_jcafb

    ::

        cd '/opt/openerp/jcafb'
        gzip -d clvhealth_jcafb_dev_2015-04-11b_063.sql.gz
        su postgres
        dropdb -i clvhealth_jcafb_tst -U postgres
        createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_tst -U postgres
        psql -f clvhealth_jcafb_dev_2015-04-11b_063.sql -d clvhealth_jcafb_tst -h localhost -p 5432 -q -U postgres
        exit

    ::
        
        cd /opt/openerp/odoo
        su openerp
        ./openerp-server -c openerp-server-man.conf

	::

		cd /opt/openerp
		su openerp
		cd /opt/openerp/odoo
		git pull
		cd /opt/openerp/clvsol_odoo_addons
		git pull
		cd /opt/openerp/clvsol_odoo_addons_l10n_br
		git pull
		cd /opt/openerp/clvsol_odoo_addons_jcafb
		git pull
		exit

* tkl-lamp-odoo-jcafb-pro

    ::
        
        git clone https://github.com/CLVsol/odoo_addons /opt/openerp/clvsol_odoo_addons --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_l10n_br /opt/openerp/clvsol_odoo_addons_l10n_br --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_l10n_br

    ::
        
        git clone https://github.com/CLVsol/odoo_addons_jcafb /opt/openerp/clvsol_odoo_addons_jcafb --branch 8.0
        chown -R openerp:openerp /opt/openerp/clvsol_odoo_addons_jcafb

    ::

        cd '/opt/openerp/jcafb'
        gzip -d clvhealth_jcafb_pro_2015-03-30a.sql.gz
        su postgres
        dropdb -i clvhealth_jcafb_pro -U postgres
        createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_pro -U postgres
        psql -f clvhealth_jcafb_pro_2015-03-30a.sql -d clvhealth_jcafb_pro -h localhost -p 5432 -q -U postgres
        exit

    ::

        cd '/opt/openerp/jcafb'
        pg_dump clvhealth_jcafb_pro -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_pro.sql
        mv clvhealth_jcafb_pro.sql clvhealth_jcafb_pro_2015-03-30a.sql
        gzip clvhealth_jcafb_pro_2015-03-30a.sql

    ::
        
        cd /opt/openerp/odoo
        su openerp
        ./openerp-server -c openerp-server-man.conf

* /opt/openerp/odoo/openerp-server.conf and /opt/openerp/odoo/openerp-server-man.conf

    ::

        addons_path = /opt/openerp/odoo/addons,/opt/openerp/oca_server_tools,/opt/openerp/clvsol_odoo_addons,/opt/openerp/clvsol_odoo_addons_l10n_br,/opt/openerp/clvsol_odoo_addons_jcafb

* Commands

    ::

        /opt/openerp/openerp.init stop
        /opt/openerp/openerp.init start

    ::
        
        cd /opt/openerp/odoo
        ./openerp-server -c openerp-server-8.0-clvhealth_jcafb.conf

    ::

        cd /opt/openerp/clvsol_odoo_clvhealth_jcafb/doc
        make clean
        make html
        
    ::

        cd /opt/openerp/clvsol_odoo_clvhealth_jcafb/project
        python install.py

.. toctree::
   :maxdepth: 2
