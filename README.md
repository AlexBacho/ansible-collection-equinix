# Equinix Ansible Collection

This is an unofficial fork of Equinix Metal collection, aiming to include other services from Equinix beyond Metal. It's still work in progress, not ready for production.

The Ansible Equinix collection includes a variety of Ansible content to help automate the management of Equinix resources. (in future: This collection is maintained by the Equinix DevRel team).

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.13.7**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

## Python version compatibility

This collection depends on:
 - [equinixmetalpy](https://github.com/t0mk/equinixmetalpy). This collection requires Python 3.8 or greater.

## Included content

<!--start collection content-->
### Inventory plugins
Name | Description
--- | ---
[equinix.cloud.metal_device](https://github.com/equinix/ansible-collection-equinix/blob/main/docs/equinix.cloud.metal_device_inventory.rst)|Equinix Metal Device inventory source

### Modules
Name | Description
--- | ---
[equinix.metal.device](https://github.com/equinix/ansible-collection-equinix/blob/main/docs/equinix.metal.device_module.rst)|Manage a bare metal server in Equinix Metal
[equinix.metal.device_info](https://github.com/equinix/ansible-collection-equinix/blob/main/docs/equinix.metal.device_info_module.rst)|Gather information about Equinix Metal devices
[equinix.metal.project](https://github.com/equinix/ansible-collection-equinix/blob/main/docs/equinix.metal.project_module.rst)|Create/delete a project in Equinix Metal
[equinix.metal.project_info](https://github.com/equinix/ansible-collection-equinix/blob/main/docs/equinix.metal.project_info_module.rst)|Gather information about Equinix Metal projects

<!--end collection content-->

## Installing this collection

You can install the Equinix Metal collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install equinix.cloud

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: equinix.cloud
```

The python module dependencies are not installed by `ansible-galaxy`.  They can
be manually installed using pip:

    pip install -r requirements.txt

or:

    pip install equinixmetalpy

## Using this collection


You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `equinix.cloud.metal_device`, or you can call modules by their short name if you list the `equinix.cloud` collection in the playbook's `collections` keyword:

```yaml
---
TODO
```

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Equinix collection repository](https://github.com/FIXTHIS).

If you require support, please email [support@equinixmetal.com](mailto:support@equinixmetal.com), visit the Equinix Metal IRC channel (#equinixmetal on freenode), subscribe to the [Equinix Metal Community Slack channel](https://slack.equinixmetal.com/) or post an issue within this repository.

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

### Testing with `ansible-test`

Running sanity tests: `ansible-test sanity --docker -v`
Running unit tests: `ansible-test units -v --docker`

Running integration tests:

```sh
cat << EOF > tests/integration/integration_config.yml
metal_api_token: <YOUR EQUINIX METAL API TOKEN>
EOF
 ansible-test integration -v --docker
 ```

### More information about contributing

- [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) - Details on contributing to Ansible
- [Contributing to Collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections) - How to check out collection git repositories correctly

## Release notes
<!--Add a link to a changelog.rst file or an external docsite to cover this information. -->

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## Publishing New Version

Prepare the release:
- Refresh the README.md: `tox -e add_docs`
- Refresh the changelog: `tox -e antsibull-changelog -- release --verbose --version 1.1.0`
- Clean up the changelog fragments.
- Commit everything and push a PR for review

Push the release:
- Tag the release: `git tag -s 1.0.0`
- Push the tag: `git push origin 1.0.0`

## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collections Checklist](https://github.com/ansible-collections/overview/blob/master/collection_requirements.rst)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
- [The Bullhorn (the Ansible Contributor newsletter)](https://us19.campaign-archive.com/home/?u=56d874e027110e35dea0e03c1&id=d6635f5420)
- [Changes impacting Contributors](https://github.com/ansible-collections/overview/issues/45)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
