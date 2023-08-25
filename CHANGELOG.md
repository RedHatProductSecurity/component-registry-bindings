# Changelog
All notable changes to this project will be documented in this file.

This project is kept in version sync with the Component Registry project, see the
[version policy](TUTORIAL.md#component-registry-compatibility) and thus a lot of
versions don't bring ground breaking changes and they rather update
the API endpoints. In such cases the version is listed without any
additions/changes/deletions.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.3.9] - 2023-08-25
### Changed
- fix bindings making lot a of uncessary calls when supplying max_results
  parameter for async list iterator which is much higher than actual results count 

## [1.3.8] - 2023-08-25
### Changed
- fix error caused by supplying empty limit to async iterator

## [1.3.7] - 2023-08-23
### Added
- operation for results count
- max_results parameter for `retrieve_list_iterator_async`
- settable maximum concurrent connections via `COMPONENT_REGISTRY_BINDINGS_MAX_CONCURRENCY`
  environmental variable
## [1.3.6] - 2023-08-22
### Added
- implement async iterator operation
## [1.3.5] - 2023-08-09
### Changed
- implement smarter pagination

## [1.3.4] - 2023-05-04

## [1.3.3] - 2023-04-04

## [1.3.2] - 2023-03-30

## [1.3.1] - 2023-03-23
### Changed
- fix pagination handling when next/previous are missing

## [1.3.0] - 2023-03-23
### Added
- add `next()`, `prev()` and `iterator()` methods for paginated
  responses to make page browsing easier

## [1.2.0-beta] - 2023-02-17
### Added
- first experimental release to the PyPI - versioning not yet fully synced with Component Registry

### Changed
- empty value (NONE) manually added to all enumarations as a temporary solution for data comming from
  Component Registry

<!-- TODO: Add links to version comparisons -->
