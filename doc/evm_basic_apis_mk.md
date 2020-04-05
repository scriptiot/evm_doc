## 3. 虚拟机对象创建API

---

### 3.1 创建浮点型evm_val_t对象

```c
evm_val_t evm_mk_number(double d)

```

### 3.2 创建整形evm_val_t对象

```c
evm_val_t evm_mk_integer(int v, int type)

```

### 3.3 创建外部字符串evm_val_t对象

```c
evm_val_t evm_mk_foreign_string(intptr_t s)

```

### 3.4 创建堆字符串evm_val_t对象

```c
evm_val_t evm_mk_heap_string(intptr_t s)

```

### 3.5 创建布尔evm_val_t对象

```c
evm_val_t evm_mk_boolean(int v)

```

### 3.6 创建脚本函数evm_val_t对象

```c
evm_val_t evm_mk_script(intptr_t s)

```

### 3.7 创建内置函数evm_val_t对象

```c
evm_val_t evm_mk_native(intptr_t s)

```

### 3.8 创建null空值evm_val_t对象

```c
evm_val_t evm_mk_null(void)

```

### 3.9 创建undefined值evm_val_t对象

```c
evm_val_t evm_mk_undefined(void)

```

### 3.10 创建obejct值evm_val_t对象

```c
evm_val_t evm_mk_object(void *ptr)

```

### 3.11 创建字节数组值evm_val_t对象

```c
evm_val_t evm_mk_buffer(void *ptr)

```

### 3.12 创建数组或列表值evm_val_t对象

```c
evm_val_t evm_mk_list(void *ptr)

```

### 3.13 创建true值evm_val_t对象

```c
evm_val_t evm_mk_true(void)

```

### 3.14 创建false值evm_val_t对象

```c
evm_val_t evm_mk_false(void)

```

### 3.15 创建NaN值evm_val_t对象

```c
evm_val_t evm_mk_nan(void)
