## 平台支持

| API     |    OS|
| :-------- | --------:|
| assert.assert| Linux，RT-Thread, Zephyr |
| assert.doesNotThrow| Linux，RT-Thread, Zephyr |
| assert.equal| Linux，RT-Thread, Zephyr |
| assert.fail|   Linux，RT-Thread, Zephyr  | 
| assert.notEqual|   Linux，RT-Thread, Zephyr  |
| assert.notStrictEqual|  Linux，RT-Thread, Zephyr  |
| assert.strictEqual|  Linux，RT-Thread, Zephyr  | 
| assert.throws|  Linux，RT-Thread, Zephyr | 


### Assert

` assert(value[, message]) `

+ {any} 测试值.
+ {any} 错误抛出时显示的消息.

```javascript
var assert = require('assert');

assert.assert(1);
// OK

assert.assert(true);
// OK

assert.assert(false);
// throws "AssertionError: false == true"

assert.assert(0);
// throws "AssertionError: 0 == true"

assert.assert(false, "it's false");
// throws "AssertionError: it's false"
```

` doesNotThrow(block[, message]) `

+ block {函数}
+ message {any} 显示的消息.

```javascript
var assert = require('assert');

assert.doesNotThrow(
  function() {
    assert.assert(1);
  }
);
// OK

assert.doesNotThrow(
  function() {
    assert.assert(0);
  }
)
// throws "AssertionError: Got unwanted exception."
```

` equal(actual, expected[, message]) `

+ actual {any} 实际值.
+ expected {any} 预期值.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.equal(1, 1);
assert.equal(1, '1');
```

` fail(actual, expected, message, operator) `

+ actual {any} 实际值.
+ expected {any} 预期值.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.equal(1, 1);
assert.equal(1, '1');
```

` notEqual(actual, expected[, message]) `

+ actual {any} 实际值.
+ expected {any} 预期值.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.notEqual(1, 2);
```

` notStrictEqual(actual, expected[, message]) `

+ actual {any} 实际值.
+ expected {any} 预期值.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.notStrictEqual(1, 2);
// OK

assert.notStrictEqual(1, 1);
// AssertionError: 1 !== 1

assert.notStrictEqual(1, '1');
// OK
```

` strictEqual(actual, expected[, message]) `

+ actual {any} 实际值.
+ expected {any} 预期值.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.strictEqual(1, 1);
// OK

assert.strictEqual(1, 2);
// AssertionError: 1 === 2

assert.strictEqual(1, '1');
// AssertionError: 1 === '1'
```

` throws(block[, expected, message]) `

+ block {Function} 在函数中抛出异常.
+ expected {Function} 预期的异常错误.
+ message {any} 显示消息.

```javascript
var assert = require('assert');

assert.throws(
  function() {
    assert.equal(1, 2);
  },
  assert.AssertionError
);
// OK

assert.throws(
  function() {
    assert.equal(1, 1);
  },
  assert.AssertionError
);
// Uncaught error: Missing exception

assert.throws(
  function() {
    assert.equal(1, 2);
  },
  TypeError
);
// AssertionError
```