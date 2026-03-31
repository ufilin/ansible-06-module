# Yandex Cloud ELK Collection

## Modules
- my_own_module

## Usage
```yaml
- hosts: localhost
  tasks:
    - name: Create file
      ufilin_collection.yandex_cloud_elk.my_own_module:
        path: /tmp/test.txt
        content: "Hello from collection!" 
