# Package documentation of <code>org.slashlib.py.eos.core.inspect</code>  

* [API Index](index.md)
* [Frameworks](../frameworks.md)
* [README](../../README.md)

## org.slashlib.py.eos.core.inspect package ([parent](org.slashlib.py.eos.core.md))

### Subpackages

No subpackages

### Module contents

org.slashlib.py.eos.core.inspect - inspection functions


#### org.slashlib.py.eos.core.inspect.iscallable(arg: Callable)

* **Returns**

    True, if arg is callable (provides ‘__call__’); False otherwise



#### org.slashlib.py.eos.core.inspect.isclass(arg: Type[T])

* **Returns**

    True, if arg is of type {class}; False otherwise



#### org.slashlib.py.eos.core.inspect.isclassmethod(cls: Type[T], arg: Callable)

* **Returns**

    True, if arg is of type [‘@classmethod](mailto:'@classmethod) def funct()’; False otherwise



#### org.slashlib.py.eos.core.inspect.isfunction(arg: Callable)
Functions, which are not and will not become bound members of classes,
are defined to be pyeos functions.


* **Returns**

    True, if arg is of type {function}; False otherwise



#### org.slashlib.py.eos.core.inspect.ismethod(arg: Callable)

* **Returns**

    True, if arg is of type {method}; False otherwise



#### org.slashlib.py.eos.core.inspect.ismethodorfunction(arg: Callable)

* **Returns**

    True, if arg is of type {method} or {function}; False otherwise



#### org.slashlib.py.eos.core.inspect.isstaticmethod(cls: Type[T], arg: Callable)

* **Returns**

    True, if arg is of type [‘@staticmethod](mailto:'@staticmethod) def funct()’; False otherwise
