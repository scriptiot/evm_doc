## 1. EVM标准化的扩展API

---

### 1.1 数据结构

+ `name`: 注册接口名称
+ `v`: 注册接口API实现

```c
typedef struct evm_builtin_t{
    const char * name;
    evm_val_t v;
}evm_builtin_t;

```

---

### 1.2 evm_native_add

> evm_native_add把evm_builtin_t列表中所有的API注册进虚拟机，成为内置属性，内置函数或内置对象。

```c
/**
 * @brief 添加内置函数列表
 * @param e，虚拟机
 * @param n，内置函数列表
 * @return 错误码
 */
evm_err_t evm_native_add(evm_t * e, evm_builtin_t * n);
```

## 2. 扩展模块注册流程

```c
/**********定义用户API*****************/



/**********注册API模块*****************/
int ecma_module(evm_t * e, int number_of_timers){

    evm_builtin_t natives[] = {
        {"set_prototype", evm_mk_native( (intptr_t)ecma_set_prototype )},
        {"isNaN", evm_mk_native( (intptr_t)ecma_isNaN )},
        {".new", evm_mk_native( (intptr_t)ecma_new )},
        {"typeof", evm_mk_native( (intptr_t)ecma_typeof )},
        {"setTimeout", evm_mk_native( (intptr_t)ecma_setTimeout )},
        {"setInterval", evm_mk_native( (intptr_t)ecma_setInterval )},
        {"clearInterval", evm_mk_native( (intptr_t)ecma_clearInterval )},
        {"atob", evm_mk_native( (intptr_t)ecma_atob )},
        {"btoa", evm_mk_native( (intptr_t)ecma_btoa )},
        {"RegExp", *ecma_regex_init(e)},
        {"Math", *Math},
        {"Object", *Object},
        {"Array", *Array},
        {"Number", *Number},
        {"String", *String},
        {"Date", *ecma_date_init(e)},
        {"JSON", *json_object},
        {NULL, EVM_VAL_UNDEFINED}
    };
    return evm_native_add(e, natives);
}

```