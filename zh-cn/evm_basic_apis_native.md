## 9. 虚拟机模块创建API

---

### 9.1 evm_native_fn函数声明

```c
/**
 * @brief evm_native_fn函数声明
 * @param e，虚拟机参数
 * @param self，绑定的内置函数
 * @param vc, 函数参数个数
 * @param v，函数参数指针
 * @return 内置函数对象
 */
typedef evm_val_t (*evm_native_fn)(void * e, evm_val_t * self, int vc, evm_val_t * v);
```


### 9.2 创建内置函数值

```
/**
 * @brief 创建内置函数值
 * @param n, 函数地址(evm_native_fn指针对象)
 * @return
 */
evm_val_t evm_mk_native(intptr_t n)
```


### 9.3 创建内置函数对象

```c
/**
 * @brief 创建内置函数对象
 * @param e，虚拟机参数
 * @param fn，绑定的内置函数
 * @param prop_len，成员长度
 * @param attr_len，属性长度
 * @return 内置函数对象
 */
evm_val_t *evm_native_function_create(evm_t *e, evm_native_fn fn, int attr_len);

```

### 9.4 添加内置函数列表

```c
/**
 * @brief 添加内置函数列表
 * @param e，虚拟机
 * @param n，内置函数列表
 * @return 错误码
 */
evm_err_t evm_native_add(evm_t * e, evm_builtin_t * n);

```


### 9.5 创建指定名称的扩展模块

```c
/**
 * @brief 创建指定名称的模块
 * @param e，虚拟机
 * @param name，名称
 * @param n，内置成员列表
 * @return 内置对象
 */
evm_val_t evm_module_create(evm_t * e, const char* name, evm_builtin_t *n);
```
