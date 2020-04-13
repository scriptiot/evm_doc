## 7. 数组或列表对象API

---

### 7.1 创建数组或列表对象

```c
/**
 * @brief 创建数组、列表
 * @param e，虚拟机参数
 * @param type，类型 GC_LIST或者GC_TUPLE(python专有)
 * @param count，长度
 * @return 数组、列表对象
 */
evm_val_t * evm_list_create(evm_t * e, int type, uint16_t len);
```

### 7.2 数组对象增加内容

```c
/**
 * @brief 数组对象增加内容
 * @param e，虚拟机参数
 * @param o，数组对象
 * @param len，增加长度
 * @param v，内容
 * @return 错误码
 */
evm_err_t evm_list_push(evm_t * e, evm_val_t * o, int len, evm_val_t *v);
```

### 7.3  数组删除最后一个内容，并返回该内容

```c
/**
 * @brief 数组删除最后一个内容，并返回该内容
 * @param e，虚拟机
 * @param o，数组对象
 * @return 被删除的内容,若删除失败，则返回undefined
 */
evm_val_t *evm_list_pop(evm_t * e, evm_val_t * o);
```

### 7.4  获取数组长度

```c
/**
 * @brief 获取数组长度
 * @param o，数组对象
 * @return 数组长度
 */
int evm_list_len(evm_val_t * o);
```

### 7.5 数组设置指定index元素的值

```c
/**
 * @brief 数组设置
 * @param e，虚拟机参数
 * @param o，数组对象
 * @param index，索引
 * @param v，值
 * @return 错误码
 */
evm_err_t evm_list_set(evm_t * e, evm_val_t * o, uint32_t index, evm_val_t v);
```

### 7.6 数组获取指定index元素内容

```c
/**
 * @brief 数组获取内容
 * @param e，虚拟机参数
 * @param o，数组对象
 * @param index，索引
 * @return 错误码
 */
evm_val_t * evm_list_get(evm_t * e, evm_val_t * o, uint32_t index);
```
