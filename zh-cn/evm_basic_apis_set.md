## 4. 虚拟机对象设置API

---

### 4.1 设置浮点型evm_val_t对象

```c
void evm_set_number(evm_val_t *v, double d)

```

### 4.2 设置整形evm_val_t对象

```c
evm_val_t evm_mk_integer(int v, int type)

```

### 4.3 设置外部字符串evm_val_t对象

```c
void evm_set_foreign_string(evm_val_t *v, intptr_t s)

```

### 4.4 设置堆字符串evm_val_t对象

```c
void evm_set_heap_string(evm_val_t *v, intptr_t s)

```

### 4.5 设置布尔evm_val_t对象

```c
void evm_set_boolean(evm_val_t *v, int b)

```

### 4.6 设置脚本函数evm_val_t对象

```c
/**
 * @brief 设置值为脚本函数
 * @param v  evm_val_t指针对象
 * @param s 函数对象指针
 */
void evm_set_script(evm_val_t *v, intptr_t s)

```

### 4.7 设置内置函数evm_val_t对象

```c
/**
 * @brief 设置值为内置函数
 * @param v evm_val_t指针对象
 * @param f 函数指针
 */
void evm_set_native(evm_val_t *v, intptr_t f)

```

### 4.8 设置null空值evm_val_t对象

```c
 void evm_set_null(evm_val_t *v)

```

### 4.9 设置undefined值evm_val_t对象

```c
void evm_set_undefined(evm_val_t *v)

```

### 4.10 设置obejct值evm_val_t对象

```c
/**
 * @brief 设置值为对象
 * @param v
 * @param 对象指针
 */
void evm_set_object(evm_val_t *v, intptr_t d)

```

### 4.11 设置字节数组值evm_val_t对象

```c
/**
 * @brief 设置值为字节数组
 * @param v
 * @param 数组指针
 */
void evm_set_buffer(evm_val_t *v, void *b)

```

### 4.12 设置数组或列表值evm_val_t对象

```c
/**
 * @brief 设置值为数组、列表
 * @param v
 * @param 数组、列表指针
 */
void evm_set_list(evm_val_t *v, void *b)

```
