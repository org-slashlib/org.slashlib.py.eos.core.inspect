# Package documentation of <code>org.slashlib.py.eos.core.inspect</code>  

inspection library for PyEOS.  
This project is in alpha state.

## content ##

* Usage
  * [Getting started guide (see 'getting started' below)](#getting-started)
* Developers
  * [API](docs/markdown/index.md)
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
Returns <code>True</code>, if <code>arg</code> is of type pyeos <code>function</code>; <code>False</code> otherwise.  

Note: In Python, function definitions in classes are not bound. Therefor they are categorized as functions, not as methods.
      PyEOS functions additionally require NOT to be a member of a class (which turns staticmethods into NOT functions)

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
      PyEOS methods additionally require to be members of classes (which turns staticmethods into methods instead of functions)

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
