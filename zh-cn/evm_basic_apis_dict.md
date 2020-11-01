## 8. obejct或dict对象API

---

### 8.1 创建数组或列表对象

```c
/**
 * @brief 创建新的对象
 * @param e，虚拟机参数
 * @param type，设置对象类型
 * @param prop_len，设置成员长度
 * @param attr_len，设置属性长度
 * @return
 */
evm_val_t *evm_object_create(evm_t * e, int type, int prop_len, int attr_len);
```

### 8.2 创建带有外部数据的新对象

```c
/**
 * @brief 创建带有外部数据的新对象
 * @param e
 * @param type
 * @param ext_data
 * @return
 */
evm_val_t *evm_object_create_ext_data(evm_t * e, int type, intptr_t ext_data);
```

### 8.3  通过类来创建对象

```c
/**
 * @brief 通过类来创建对象
 * @param e，虚拟机参数
 * @param o，类对象
 * @return 创建的新对象
 */
evm_val_t * evm_object_create_by_class(evm_t * e, int type, evm_val_t * o);
```

### 8.4  解除对象引用，强制垃圾回收

```c
/**
 * @brief 解除对象引用，强制垃圾回收
 * @param e
 * @param o
 */
void evm_object_deref(evm_t * e, evm_val_t * o);
```

### 8.5 通过字符串名称对象查找成员

```c
/**
 * @brief 通过字符串名称对象查找成员
 * @param e，虚拟机参数
 * @param o，对象
 * @param key，字符串名称
 * @param depth，depth大于0表示查找范围包括父类，否则不包括父类
 * @return 成员，查找失败则返回undefined
 */
evm_val_t * evm_prop_get(evm_t *e, evm_val_t * o, const char* key, int depth);
```

### 8.6 通过key索引查找成员

```c
/**
 * @brief 通过字符串名称对象查找成员
 * @param e，虚拟机参数
 * @param o，对象
 * @param key，字符串索引
 * @param depth，depth大于0表示查找范围包括父类，否则不包括父类
 * @return 成员，查找失败则返回undefined
 */
evm_val_t * evm_prop_get_by_key(evm_t * e, evm_val_t *obj, 
                                uint32_t key, int depth);
```

### 8.6 通过索引位置获取对象成员

```c
/**
 * @brief 通过索引位置获取对象成员
 * @param e
 * @param o
 * @param index
 * @return
 */
evm_val_t * evm_prop_get_by_index(evm_t * e, evm_val_t * o, int index);
```

### 8.6 按顺序添加对象成员

```c
/**
 * @brief 按顺序添加对象成员
 * @param e，虚拟机参数
 * @param o，对象
 * @param index, 索引
 * @param key，字符串名称
 * @param v，成员值
 * @return 正确返回ec_ok，错误返回ec_index
 */
evm_err_t evm_prop_set(evm_t * e, evm_val_t * o, uint32_t index, 
                       const char *key, evm_val_t v);
```

### 8.7 通过索引index，设置对象成员的key和value

```c
/**
 * @brief 通过索引index，设置对象成员的key和value
 * @param e，虚拟机
 * @param o，对象
 * @param index，索引
 * @param key，字符串key值
 * @param v，成员值
 * @return 正确返回ec_ok，错误返回ec_index
 */
evm_err_t evm_prop_set_key_value(evm_t * e, evm_val_t * o, uint32_t index, 
                                 uint16_t key, evm_val_t v);
```

### 8.8 通过对象名称设置对象成员

```c
/**
 * @brief 对象成员设置
 * @param e，虚拟机参数
 * @param o，对象
 * @param key，字符串名称
 * @param v，成员值
 * @return 正确返回ec_ok，错误返回ec_key
 */
evm_err_t evm_prop_set_value(evm_t * e, evm_val_t * o, 
                             const char* key, evm_val_t v);
```

### 8.9 通过对象名称追加对象成员

```c
/**
 * @brief 对象追加成员
 * @param e，虚拟机参数
 * @param o，对象
 * @param key，字符串名称
 * @param v，值
 * @return 错误码
 */
evm_err_t evm_prop_append(evm_t * e, evm_val_t * o, char * key, evm_val_t * v);
```

### 8.10 通过索引追加成员

```c
/**
 * @brief 对象通过索引追加成员
 * @param e，虚拟机参数
 * @param o，对象
 * @param key，字符串索引
 * @param v，值
 * @return 错误码
 */
evm_err_t evm_prop_append_with_key(evm_t * e, evm_val_t * o, int key, 
                                   evm_val_t * v);
```

### 8.11 通过索引设置成员值

```c
/**
 * @brief 通过索引设置成员值
 * @param e，虚拟机
 * @param o，对象
 * @param index，索引
 * @param v，值
 * @return 错误码
 */
evm_err_t evm_prop_set_value_by_index(evm_t * e, evm_val_t *o, 
                                      uint32_t index, evm_val_t v);
```

### 8.12 通过索引设置成员值

```c
/**
 * @brief 通过索引获取成员的名称索引值
 * @param e，虚拟机
 * @param o，对象
 * @param index，索引
 * @return 名称索引值，通过evm_string_get获取索引对应的字符串内容
 */
uint32_t evm_prop_get_key_by_index(evm_t * e, evm_val_t * o, int index);
```
### 8.13 通过索引设置成员的名称索引值

```c
/**
 * @brief 通过索引设置成员的名称索引值
 * @param e，虚拟机参数
 * @param o，对象
 * @param index，索引
 * @param key，字符串索引值
 */
void evm_prop_set_key_by_index(evm_t * e, evm_val_t * o, int index, 
                               uint32_t key);
```
### 8.14 获取对象成员个数长度

```c
/**
 * @brief 获取对象成员个数长度
 * @param o，对象
 * @return
 */
int evm_prop_len(evm_val_t * o);
```
