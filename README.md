pivot_it
==============


A command line tool useful for pivoting CSV files.

### Requirements
Packages: Just Click. So simple

Python: Python3 is great (not tested with 2)


### Installation

Download the source code and install it

```
git clone https://github.com/LionelR/pivot_it.git
cd pivot_it
python setup.py install
```

... or ask Deep Thought to install it by:

```
pip install git+https://github.com/LionelR/pivot_it.git
```

These commands will create a executable on your system (thanks to the awesome Click package).


### Usage

For help, call help (or better call Saul)

```
pivot_it --help

Usage: pivot_it [OPTIONS] FIN FOUT

  Pivot some data contained inside a CSV file after a specified column
  number and write the result to another file. The original CSV file must
  have a header on the first line.

Options:
  -c, --column TEXT     Column number or name after which to make the pivot.
                        Default to 1
  -s, --separator TEXT  CSV separator. Default to comma
  -k, --ckey TEXT       New key column name, containing the old columns names.
                        Default to 'key
  -v, --cval TEXT       New value column name, containing the pivoted values.
                        Default to 'value'
  --help                Show this message and exit.
```

Say you have a CSV file named "weights.csv" containing weights of some users by year stored in line mode :

<pre>
Name,City,2000,2001,2002
Carles,London,78,77,79
Nancy,Paris,55,53,52
</pre>

To pivot this (horrible) file after the second column to a more database-like format (column mode), just do:

```
pivot_it --column 2 weights.csv pivot_weights.csv
```

pivot_weights.csv contents:

<pre>
Name,City,key,value
Carles,London,2000,78
Carles,London,2001,77
Carles,London,2002,79
Nancy,Paris,2000,55
Nancy,Paris,2001,53
Nancy,Paris,2002,52
</pre>

The `--column` option takes the column number after which to make the pivot, or his name.
`--ckey` and `cval` are used to rename the defaults new columns, so

```
pivot_it --column City --ckey Year --cval Weight weights.csv pivot_weights.csv
```

will produce the same resulting file as previously, with header
<pre>
Name,City,Year,Weight
</pre>

