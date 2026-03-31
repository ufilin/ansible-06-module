# Ansible Collection for Yandex Cloud ELK

This repository contains Ansible collection with custom modules for Yandex Cloud and ELK stack.

## Collection Structure

- `yandex_cloud_elk/` - The main collection
  - `plugins/modules/my_own_module.py` - Module for creating files
  - `roles/my_file_role/` - Example role using the module

## Installation

### From archive
```bash
ansible-galaxy collection install ufilin_collection-yandex_cloud_elk-1.0.0.tar.gz
```

### From source
```bash
git clone https://github.com/ufilin/ansible-06-module.git
cd ansible-06-module
ansible-galaxy collection build
ansible-galaxy collection install ufilin_collection-yandex_cloud_elk-*.tar.gz
```

## Usage

```yaml
- hosts: localhost
  tasks:
    - name: Create file
      ufilin_collection.yandex_cloud_elk.my_own_module:
        path: /tmp/test.txt
        content: "Hello from collection!"
```

## License

GPL-3.0-only
