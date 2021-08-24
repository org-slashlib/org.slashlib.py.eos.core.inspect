# org.slashlib.py.eos.core.inspect #

inspection library for PyEOS.  
This project is in alpha state.

## content ##

* Usage
  * [Getting started guide (see 'getting started' below)](#getting-started)
* Developers
  * [Frameworks used for building, testing, etc.](docs/frameworks.md)

## getting started ##

### prerequisites ###

<p>This project requires python 3.9 or newer and upgrading pip and setuptools.</p>
<code>python -m pip install --upgrade pip</code><br />
<code>pip install --upgrade setuptools</code>

### install ###

<code>pip install org.slashlib.py.eos.core.inspect</code>

## usage ##

<code>org.slashlib.py.eos.core.inspect</code> is a package required by PyEOS.

### <code>iscallable</code> ###
Returns <code>True</code>, if <code>arg</code> is callable (provides <code>\_\_call\_\_</code>); <code>False</code> otherwise.
<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def iscallable( arg: Callable ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>

### <code>isclass</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>class</code>; <code>False</code> otherwise.
<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def isclass( arg: Type[ T ]) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>arg</code></td>
      <td>Any type definition</td>
      </tr>
</table>

### <code>isclassmethod</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>@classmethod def funct()</code>; <code>False</code> otherwise.
<table style="padding:0">
  <tr><td>Signature</td>
      <td colspan="2"><code>def isclassmethod( cls: Type[ T ], arg: Callable ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>cls</code></td>
      <td>A class</td>
      </tr>
  <tr><td></td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>


### <code>isfunction</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>function</code>; <code>False</code> otherwise.  

Note: In Python, function definitions in classes are not bound. Therefor they are categorized as functions, not as methods.

Future: This will change in future, to enable recognition of functions which belong to classes and such, that do not belong to classes (like inner functions, anonymous functions, ...whatever)

<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def isfunction( arg: Callable ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>

### <code>ismethod</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>method</code>; <code>False</code> otherwise.

Note: In Python, methods are bound functions. <code>ismethod</code> will not reveal function definitions in classes as methods.  

Future: This will change in future, to enable recognition of functions which belong to classes and such, that do not belong to classes (like inner functions, anonymous functions, ...whatever)

<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def ismethod( arg: Callable ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>

### <code>ismethodorfunction</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>method</code>or<code>function</code>; <code>False</code> otherwise.

<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def ismethodorfunction( arg: Callable  ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>

### <code>isstaticmethod</code> ###
Returns <code>True</code>, if <code>arg</code> is of type <code>@staticmethod def funct()</code>; <code>False</code> otherwise.

<table>
  <tr><td>Signature</td>
      <td colspan="2"><code>def isstaticmethod( cls: Type[ T ], arg: Callable ) -> bool</code></td>
      </tr>
  <tr><td>Parameters</td>
      <td><code>cls</code></td>
      <td>A class</td>
      </tr>
  <tr><td></td>
      <td><code>arg</code></td>
      <td>Any callable</td>
      </tr>
</table>
