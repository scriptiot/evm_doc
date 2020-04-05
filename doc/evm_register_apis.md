## 1. 什么是虚拟机注册接口

> 虚拟机注册接口是指用户需要根据自身平台适配的API 

---

### 1.1 打印接口

> 用于打印输出调试信息

+ 接口格式

```
void (*evm_print)(const char *fmt, ...);
```

+ 注册接口

```
void evm_register_print(intptr_t fn);
```

---

### 1.2 外部内存申请接口

> 类似C语言中的`malloc`接口 

+ 接口格式

```
void * (*evm_malloc)(int size);
```

+ 注册接口

```
void evm_register_malloc(intptr_t fn);
```

---

### 1.3 外部内存释放接口

> 类似C语言中的`free`接口 

+ 接口格式

```
void * (*evm_free)(int size);
```

+ 注册接口

```
void evm_register_free(intptr_t fn);
```

---

### 1.4 虚拟机文件加载接口

> 用于虚拟机打开对应的脚本语言文件

+ 接口格式

```
const char * vm_load(evm_t * e, char * path, int type);
```

+ 注册接口

```
void evm_register_file_load(intptr_t fn);
```

---

## 2. 用法示例

> 参考 `main.c` 中实现 

---

### 2.1 接口实现
```c
const char * vm_load(evm_t * e, char * path, int type)
{
    int file_name_len = strlen(path) + 1;
    char* buffer = NULL;
    if(type == EVM_LOAD_MAIN){
        char * module_name = evm_malloc(file_name_len);
        if( !module_name ) return NULL;
        sprintf(module_name, "%s", path);
        sprintf(e->file_name, "%s", path);
        buffer = open(e, module_name);
        evm_free(module_name);
    } else {
        for(int i=0; i< modules_paths_count; i++){
            int len = strlen(modules_paths[i]) + 1 + file_name_len;
            char* modules_path = evm_malloc(len);
            sprintf(modules_path,  "%s/%s", modules_paths[i], path);
            sprintf(e->file_name, "%s", path);
            buffer = open(e, modules_path);
            evm_free(modules_path);
            if (buffer){
                break;
            }
        }

        if (!buffer){
            const char * module_path = "../../evm/test/eJS/%s";
            int file_name_len = strlen(module_path) + strlen(path) + 1;
            char * module_name = evm_malloc(file_name_len);
            sprintf(module_name,  module_path, path);
            sprintf(e->file_name, "%s", path);
            buffer = open(e, module_name);
            evm_free(module_name);
        }
    }
    return buffer;
}


void * vm_malloc(int size)
{
    void * m = malloc(size);
    if(m) memset(m, 0 ,size);
    return m;
}

void vm_free(void * mem)
{
    if(mem) free(mem);
}

```

---

### 2.2 接口注册

```c
int main(int argc, char *argv[])
{
	// 注册虚拟机接口
    evm_register_free((intptr_t)vm_free);
    evm_register_malloc((intptr_t)vm_malloc);
    evm_register_print((intptr_t)printf);
    evm_register_file_load((intptr_t)vm_load);

    ...
}
```
