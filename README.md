pivot_it
==============


A command line tool useful for pivoting a CSV file.

### Requirements
Packages: Just Click. So simple...

Python: Python3 is great (not tested with 2)


### Installation

After that, you can download the source code and install it

```
git clone https://github.com/LionelR/pg_dependences.git
cd pg_dependences
python setup.py install
```

... or ask Deep Thought to install it with:

```
pip install git+https://github.com/LionelR/pg_dependences.git
```

These commands normally will create a executable on your system (thanks to the great Click package).


### Usage

For help, call help (or better call Saul)

```
pg_dependences --help
Usage: pg_dependences.py [OPTIONS] SCHEMA

  Report counts of linked objects and foreign keys at the first level for
  all tables and views in the specified schema. With the --table option,
  generates a pdf graph presenting for this specified top level table (or
  view) all the dependents objects in a cascaded style, i.e. all linked
  views and functions using these objects, and all tables using foreign keys
  to this top level table, if any.

Options:
  -u, --user TEXT      Database user name. Default to current user
  -P, --password TEXT  User password. WIll be prompted if not set
  -h, --host TEXT      Database host address. Default to localhost
  -d, --database TEXT  Database name. Default to current user name
  -p, --port INTEGER   Database port to connect to. Default to 5432
  -v, --verbose        Verbose mode. Only relevant with --table option
  -t, --table TEXT     Generate a detailled cascading graph of all objects
                       related to this table or view
  -o, --output TEXT    Directory where to put the resulting PDF file. Default
                       to home directory
  --help               Show this message and exit.
```

Getting a summary of linked objects and foreign keys counts of all tables and views in a schema:

```
pg_dependences -h myhost -d mybase myschema
```

You'll be asked for the database password if not set on the command line, like for the user name if no one is given and the environnement variable is empty.

<pre>
In schema tertiaire                first stage links    foreign keys
-------------------------------  -------------------  --------------
branche                                            2               6
chaufferies_collectives                            3               0
clap                                               1               0
cor_cp_numcom                                      2               0
cor_naf_branche                                    1               0
cu_regionaux                                       1               0
enseignement                                       2               0
fe_tertiaire                                       1               0
sante                                              1               0
social                                             1               0
tc_conso_botup                                     2               0
tc_conso_corrigees_botup                           3               0
tc_emi                                             1               0
tertiaire_reference                                0               2
verif_tc_conso_corrigees_botup                     0               0
vue1_effectifs_non_sante_social                    1               0
vue2_social_numcom                                 0               0
vue3_capacite_sante_social                         1               0
vue4_conso                                         2               0
vue5_fe_tertiaire_fin                              3               0
vue6_emi                                           1               0
vue7_conso_020100_fin                              0               0
vue8_emi_020100_fin                                0               0
vue_test1_bouclage_conso                           0               0
vue_test2_bouclage_emi                             0               0
vue_validation_capacite_social                     0               0
</pre>

For a particular object in the schema, we can now generate a graph showing all
dependencies in a cascaded way.

```
pg_dependences -h myhost -d mybase -t branche -v myschema
```
The `-v` for verbose option will give a detail of what is finded on the terminal.

<pre>
OBJECT: tertiaire.branche
        - USED IN VIEW: tertiaire.vue2_social_numcom
        - USED IN VIEW: tertiaire.vue3_capacite_sante_social
OBJECT: tertiaire.vue3_capacite_sante_social
        - USED IN VIEW: tertiaire.vue4_conso
OBJECT: tertiaire.vue4_conso
        - USED IN VIEW: tertiaire.vue7_conso_020100_fin
        - USED IN VIEW: tertiaire.vue_test1_bouclage_conso
OBJECT: tertiaire.branche
        - REFERENCED BY: tertiaire.chaufferies_collectives
        - REFERENCED BY: tertiaire.cu_regionaux
        - REFERENCED BY: tertiaire.enseignement
        - REFERENCED BY: tertiaire.tc_conso_botup
        - REFERENCED BY: tertiaire.tc_conso_corrigees_botup
        - REFERENCED BY: tertiaire.tc_emi
</pre>

And the resulting graph will be saved under your home directory by default
(can be changed with the `-o` option), with file name formated like schema.table.gv.pdf

![Example graph](examples/example.png?raw=true)

Graph legend:
<table>
<tr>
<th>object</th>
<th>attribute</th>
</tr>

<tr>
<td>table</td>
<td>color:white, border:black</td>
</tr>

<tr>
<td>view</td>
<td>color:light-grey</td>
</tr>

<tr>
<td>function</td>
<td>color:light-blue</td>
</tr>

<tr>
<td>foreign keys columns</td>
<td>on edge</td>
</tr>
</table>