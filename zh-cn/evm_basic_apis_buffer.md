## 6. buffer对象API

---

### 6.1 创建字节数组

```c
/**
 * @brief 创建字节数组
 * @param e,虚拟机参数
 * @param len,数组长度
 * @return 字节数组对象
 */
evm_val_t *evm_buffer_create(evm_t *e, int len);
```

### 6.2 获取buffer对象的数据地址
```c
/**
 * @brief 获取buffer对象的数据地址
 * @param o
 * @return
 */
uint8_t * evm_buffer_addr(evm_val_t * o);
```
### 6.3 获取字节数组长度
```c
/**
 * @brief 获取字节数组长度
 * @param v,字节数组对象
 * @return 字节数组长度
 */
int evm_buffer_len(evm_val_t * o);
```
### 6.4 字节数组内容设置
```c
/**
 * @brief 字节数组内容设置
 * @param o，字节数组对象
 * @param index，索引
 * @param len，长度
 * @param buffer，写入内容缓存数组
 * @return 虚拟机错误码
 */
evm_err_t evm_buffer_set(evm_val_t * o, uint8_t * buffer, uint32_t index, uint32_t len);
```
