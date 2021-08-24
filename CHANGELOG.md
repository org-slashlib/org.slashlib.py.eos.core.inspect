# Changelog #

All notable changes to this project will be documented in this file.

## [Unreleased] ##

### Added ###

- No additions yet

### Fixed ###

- No Fixes yet

## [0.0.2] - 2021-08-25 ##

### Added ###
- better testing
- iscallable to check weather callables implement __call__
- utils.py with 'get_local_part' for returning the local part of qualified
  function names

### Fixed ###
- isfunction only returns true for functions which are 'NOT class members'
- ismethod only returns true for functions which are 'class members'
- isfunction and ismethod do not care about bindings anymore

## [0.0.1] - 2021-08-13 ##
Initial release (GIT)
