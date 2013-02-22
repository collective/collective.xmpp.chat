Troubleshooting:
================

ejabberd: Module could not be loaded
------------------------------------

Sometimes after running buildout you might get errors like the following: ::

    ERROR REPORT==== 21-Jun-2012::11:05:25 ===
    ** State machine <0.380.0> terminating
    ** Last event in was connect
    ** When State == connecting
    **      Data  == {state,undefined,mysql,30000,"localhost",undefined,{0,{[],[]}}}
    ** Reason for termination =
    ** {'module could not be loaded',
        [{mysql_conn,start,
                ["localhost",3306,"sqluser","sqlpassword","ejabberd",
                #Fun<ejabberd_odbc.6.56507233>]},
            {ejabberd_odbc,mysql_connect,5},
            {ejabberd_odbc,connecting,2},
            {p1_fsm,handle_msg,10},
            {proc_lib,init_p_do_apply,3}]}


This would be because you are missing some .beam files required by ejabberd. Check the error message
to see what exactly is missing. If it's mysql related the you need to copy over the mysql .beam files.

See :ref:`enable-mysql-support-for-ejabberd` .

If the message is *Problem starting the module mod_archive_odbc* then you know it's the beam files
for mod_archive.

See :ref:`enable-mod_archive-support-for-ejabberd` .
