## 1. 虚拟机如何启动


|  启动流程    |  代码示图  |
| :--------: | :--------: |
|![evm_start](./image/evm_start_1.png)|![evm_start](./image/evm_start_2.png)|
---

### 1.1 注册虚拟机API

```c
// 注册平台相关的虚拟机API
evm_register_malloc((intptr_t)vm_malloc);
evm_register_free((intptr_t)vm_free);
evm_register_file_load((intptr_t)vm_load);
evm_register_print((intptr_t)printf);
```

+ 注册外部内存申请接口 evm_register_malloc

```c
/**
 * @brief 外部内存申请接口
 * @param size, 申请内存大小
 * @return 内存成功分配的对象指针
 */
void * vm_malloc(int size)
{
    void * m = malloc(size);
    if(m) memset(m, 0 ,size);
    return m;
}
```

+ 注册外部内存释放接口 evm_register_free

```c
/**
 * @brief 外部内存释放接口
 * @param mem, 需要释放的对象指针
 * @return
 */
void vm_free(void * mem)
{
    if(mem) free(mem);
}
```

+ 注册脚本加载接口 evm_register_file_load

```c
/**
 * @brief 加载main运行脚本和加模块脚本
 * @param e, 虚拟机对象
 * @param path, 脚本路径
 * @param type, EVM_LOAD_MAIN代表main运行脚本，非EVM_LOAD_MAIN代表加载模块
 * @return
 */
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
```

+ 注册打印接口 evm_register_print

```c
// 标准的c语言printf接口
printf
```

### 1.2 初始化虚拟机

> 用户自定义申请堆栈大小和最大加载模块个数，用户依据适配平台自定义分配

| 配置项      |    默认值| 备注|
| :-------- | --------:| :--: |
| heap_size| 1000 * 1000 * 1024 |  堆大小   |
| stack_size|   10000 * 1024 |  栈大小  |
| module_size|    10 | 最大加载模块个数  |


```c
// 初始化虚拟机
int32_t head_size = 10 *1000 * 1024;
int32_t stack_size = 10000 * 1024;
int32_t module_size = 10;
evm_t * env = (evm_t*)malloc(sizeof(evm_t));
memset(env, 0, sizeof(evm_t));
int err = evm_init(env, head_size, stack_size, module_size, EVM_VAR_NAME_MAX_LEN, EVM_FILE_NAME_LEN);
```

### 1.3 加载虚拟机模块

> 根据项目需求，加载用户指定的模块
```c
    // 加载ecma模块
    ecma_module(env, 10);
```

### 1.4 启动REPL调试

> 用户根据自身需求是否启动REPL模块，在线调试程序

```c
    // 启动REPL调试
    if (argc == 1){
        help();
        evm_repl_run(env, 1000, EVM_LANG_JS);
    }
```

### 1.5 加载js/py/lua等脚本文件

> 加载入口main脚本文件

```c
    err = evm_boot(env, argv[1]);

    if (err == ec_no_file){
        printf(QMAKE_TARGET": can't open file '%s': [Errno 2] No such file or directory\n", argv[1]);
        exit(1);
    }

    if(err) {return err;}
```

### 1.6 启动虚拟机

> 启动虚拟机，运行入口脚本

```c
    // 启动虚拟机
    err = evm_start(env);
```


## 2. 完整的main.c示例文件

[完整的main.c文件](https://github.com/scriptiot/evm/blob/master/ejs/main.c)

```c
int main(int argc, char *argv[])
{
    // 注册平台相关的虚拟机API
    evm_register_free((intptr_t)vm_free);
    evm_register_malloc((intptr_t)vm_malloc);
    evm_register_print((intptr_t)printf);
    evm_register_file_load((intptr_t)vm_load);

    // 初始化虚拟机
    int32_t head_size = 10 *1000 * 1024;
    int32_t stack_size = 10000 * 1024;
    int32_t module_size = 10;
    evm_t * env = (evm_t*)malloc(sizeof(evm_t));
    memset(env, 0, sizeof(evm_t));
    int err = evm_init(env, head_size, stack_size, module_size, EVM_VAR_NAME_MAX_LEN, EVM_FILE_NAME_LEN);

    // 加载ecma模块
    ecma_module(env, 10);

    // 启动REPL调试
    if (argc == 1){
        help();
        evm_repl_run(env, 1000, EVM_LANG_JS);
    }

    // 加载js/py/lua等脚本文件
    err = evm_boot(env, argv[1]);

    if (err == ec_no_file){
        printf(QMAKE_TARGET": can't open file '%s': [Errno 2] No such file or directory\n", argv[1]);
        exit(1);
    }

    if(err) {return err;}

    // 启动虚拟机
    err = evm_start(env);

    return err;
}
```
