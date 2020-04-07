## 5. 字符串操作API

---

### 5.1 通过key索引查找字符串

```c
/**
 * @brief 通过key索引查找字符串
 * @param e，虚拟机
 * @param key，索引
 * @return 字符串，若找不到，返回NULL
 */
char *evm_string_get(evm_t * e, uint16_t key);
```

### 5.2 通过字符串名称查找该名称的索引值
```c
/**
 * @brief 通过字符串名称查找该名称的索引值
 * @param e,虚拟机
 * @param str，字符串
 * @return
 */
int evm_str_lookup(evm_t * e, const char *str);
```

### 5.3 插入字符串到常量池
```c
/**
 * @brief 插入字符串到常量池
 * @param e,虚拟机
 * @param str，字符串
 * @param alloc，1表示复制字符串对象，0表示不复制
 * @return 常量池索引位置
 */
uint16_t evm_str_insert(evm_t *e, const char *str, int alloc);
```
