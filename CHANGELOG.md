<a name="0.6.8"></a>
# [Supports WHO and exon Reduction Types (0.6.8)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.8) - 24 Sep 2021

- Handle cases when there is no typing and when redux fails.
- added `exon` resolution group 
- added `W` resolution group
- Fix validation issues with empty alleles, NNNNs, and non-allelic values. 
- pyard-import can refresh MACs and rebuild databases

[Changes][0.6.8]


<a name="0.6.6"></a>
# [handle invalid/blank input (0.6.6)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.6) - 29 Jul 2021

handle cases with no input and redux fails

[Changes][0.6.6]


<a name="0.6.5"></a>
# [updates to pyard-reduce-csv and unit tests (0.6.5)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.5) - 17 Jun 2021


    Use pyard-reduce-csv command to reduce a CSV file based on a JSON config file.
    Use db_version 3440 in unit test to match behave tests
    Re-run the tests again so local db is used.



[Changes][0.6.5]


<a name="0.6.4"></a>
# [DRBX Mapping and Cw Serology (0.6.4)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.4) - 16 Jun 2021

 - Map DRB3, DRB4 and DRB5 typings to DRBX. #82 
 - Change C to Cw for serology; #84 
 - Return '' for invalid MACs #84 

[Changes][0.6.4]


<a name="0.6.3"></a>
# [0.6.3 release (0.6.3)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.3) - 09 Jun 2021

 addresses one-to-many relationship from 2d to lg/lgx

[Changes][0.6.3]


<a name="0.6.2"></a>
# [Fixes serology mappings for broad to include alleles in the split (0.6.2)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.2) - 07 Jun 2021

Fixes serology mappings for broad to include alleles in the split.

[Changes][0.6.2]


<a name="0.6.1"></a>
# [V2 to V3 Mapping (0.6.1)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.1) - 04 Feb 2021


   - Heuristically predict V3 from V2 when not in exceptional case list
   - Make is_XX a public method on the ARD object
   - Update README and fix bug in pyard-import for importing into Latest


[Changes][0.6.1]


<a name="0.6.0"></a>
# [Nomenclature versioning (0.6.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.6.0) - 08 Dec 2020

adds nomenclature versioning, cmdline options, GL string examples

[Changes][0.6.0]


<a name="0.5.1"></a>
# [fix mac expansion (0.5.1)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.5.1) - 30 Nov 2020

Fix serology mapping and mac expansions

[Changes][0.5.1]


<a name="0.4.1"></a>
# [Upgrade Pandas to 1.1.4 (0.4.1)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.4.1) - 03 Nov 2020

Update pandas 1.1.4

   - Pandas `1.1.2` doesn't work with Python 3.9. Upgrade Pandas to `1.1.4` which works with Python 3.8 and 3.9


[Changes][0.4.1]


<a name="0.4.0"></a>
# [ Support reduction of serologically typed GL String (0.4.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.4.0) - 22 Oct 2020

Uses WMDA `rel_dna_ser.txt` for the corresponding version of IMGT database to produce serology mapping

[Changes][0.4.0]


<a name="0.3.0"></a>
# [Use sqlite3 database for reference data (0.3.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.3.0) - 15 Oct 2020

 Use sqlite3 database for data 

Offload MAC codes from memory to sqlite3 database (natively supported by Python) to reduce
memory footprint. All MAC lookups happen through the db. The alleles and G group expansions
are still held in memory.

In addition, all generated data is saved as tables in the same database. This leads to one
file for storing all reference data in a standard format.

This led to drastic reduction in memory usage and startup time.

|Version |First Time| Prebuilt Data|
|:--|--:|--:|
| 0.1.0 | 10.5 sec |  4.92 sec|
| 0.2.0 | 814 msec |  598 msec|
| 0.3.0 | 24.1 msec | 24.7 msec |

Heap memory used by ARD reference data after `ard = pyard.ARD(3290)`

|Version |Memory (MB) |
|:--|--:|
| 0.1.0 | 2977.86 MB |
| 0.2.0 | 420.76 MB |
| 0.3.0 | 3.74 MB |


[Changes][0.3.0]


<a name="0.2.0"></a>
# [rearrange data in memory (0.2.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.2.0) - 14 Oct 2020

This release rearranges how memory is used especially MAC codes and a lot of cleanup.

[Changes][0.2.0]


<a name="0.1.0"></a>
# [load_mac_file flag to load MAC file (0.1.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.1.0) - 01 Oct 2020

 Rename download_mac flag

  - Rename `download_mac` ARD flag to `load_mac_file` as it properly describes what it does.
  - Remove dead code
  - Reformat code and fix some comments
  - Version bumped to `0.1.0`
  - Updated `pandas` to `1.1.2`

[Changes][0.1.0]


<a name="0.0.21"></a>
# [fix tests and sorting (0.0.21)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.21) - 09 Sep 2020

fixes test and also a bug in 4th field sorting

[Changes][0.0.21]


<a name="0.0.20"></a>
# [allow P and G as input, fix lg and lgx behavior (0.0.20)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.20) - 09 Sep 2020

This release fixes the behavior of lg and lgx to always reduce to 2-field.
It also allows P and G alleles as input

[Changes][0.0.20]


<a name="0.0.18"></a>
# [Fixes G-codes expansion (0.0.18)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.18) - 29 Jul 2020

Fixes G-codes expansion when smart sorting.

[Changes][0.0.18]


<a name="0.0.17"></a>
# [Specify path for temporary files (0.0.17)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.17) - 22 Jul 2020

You can specify path when creating ARD object.
```
ard = ARD('3290', data_dir='/tmp/py-ard')
```

[Changes][0.0.17]


<a name="0.0.16"></a>
# [version 0.0.16 (0.0.16)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.16) - 09 Jul 2020

update MAC location and version to 0.0.16

[Changes][0.0.16]


<a name="0.0.15.0"></a>
# [update to MAC location (0.0.15.0)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.15.0) - 28 May 2020



[Changes][0.0.15.0]


<a name="0.0.15"></a>
# [update to MAC location (0.0.15)](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.15) - 28 May 2020

yes

[Changes][0.0.15]


<a name="0.0.14"></a>
# [0.0.14](https://github.com/nmdp-bioinformatics/py-ard/releases/tag/0.0.14) - 14 Apr 2020

- Support for Python 3.7
- Broad XX enhancement 
- p Performance improvements

[Changes][0.0.14]


[0.6.8]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.6...0.6.8
[0.6.6]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.5...0.6.6
[0.6.5]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.4...0.6.5
[0.6.4]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.3...0.6.4
[0.6.3]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.2...0.6.3
[0.6.2]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.1...0.6.2
[0.6.1]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.5.1...0.6.0
[0.5.1]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.4.1...0.5.1
[0.4.1]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.21...0.1.0
[0.0.21]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.20...0.0.21
[0.0.20]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.18...0.0.20
[0.0.18]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.17...0.0.18
[0.0.17]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.16...0.0.17
[0.0.16]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.15.0...0.0.16
[0.0.15.0]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.15...0.0.15.0
[0.0.15]: https://github.com/nmdp-bioinformatics/py-ard/compare/0.0.14...0.0.15
[0.0.14]: https://github.com/nmdp-bioinformatics/py-ard/tree/0.0.14

 <!-- Generated by changelog-from-release -->